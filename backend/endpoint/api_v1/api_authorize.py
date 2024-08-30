
from fastapi import BackgroundTasks, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from core.authorize import create_access_token,user_scopes,verify_user_credentials,get_user_permissions, scope_contains
from response.std import URFRouter
from model.User import UserRegisterSchema, User
from model.EmailRegister import EmailRegister
from core.setting import config
from core.utils import get_random_string,send_email_confirmation_link

authorize_router = URFRouter(prefix="/authorize")

@authorize_router.post("/token",description="authorize user and get token", name="user authorize api")
async def secure_endpoint_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username and form_data.password:
        # get user and verify credentials
        credential = await verify_user_credentials(form_data.username, form_data.password)
        if not credential:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # check permissions
        user_scopes = await get_user_permissions(form_data.username)
        if not scope_contains(form_data.scopes, user_scopes):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        
        # create token
        jwt_data = {
            "sub": credential.user_id,
            "scope": form_data.scopes
        }
        token = create_access_token(jwt_data)
        return {"access_token": token, "token_type": "bearer"}

@authorize_router.get("/scopes",description="get user scopes", name="user scopes api")
async def secure_endpoint_get_system_scopes():
    return user_scopes


@authorize_router.post("/register")
async def secure_endpoint_register_user(new_user: UserRegisterSchema,background_tasks: BackgroundTasks):
    if not config.ENABLE_USER_REGISTRATION:
        raise HTTPException(status_code=403, detail="User registration is disabled")
    # create a new user
    try:
        await User.create(username=new_user.username, password=new_user.password, email=new_user.email, is_active=False)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"User registration failed, you may have already registered with this email. Error: {str(e)}")
    # create a new email register
    hex_key = get_random_string(16)
    await EmailRegister.create(email=new_user.email, hashcode=hex_key)
    background_tasks.add_task(
        send_email_confirmation_link,  # this is a conroutine function
        new_user.email,
        hex_key
    )
    return {"message": "User registration successful, please check your email for confirmation link"}


@authorize_router.get("/regcheck")
async def secure_endpoint_check_registration(hashcode: str):
    if not config.ENABLE_USER_REGISTRATION:
        raise HTTPException(status_code=403, detail="User registration is disabled")
    # check if hashcode exists
    email_register = await EmailRegister.filter(hashcode=hashcode).first()
    if not email_register:
        raise HTTPException(status_code=404, detail="Invalid hashcode")
    # check if user exists
    user = await User.filter(email=email_register.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # check if user is already active
    if user.is_active:
        raise HTTPException(status_code=400, detail="User is already active")
    # activate user and delete email register
    await email_register.delete()
    user.is_active = True
    await user.save()
    return {"message": "User registration successful"}

