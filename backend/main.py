
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from response.exceptions import global_exception_handler
from response.std_resp import URFRouter

app = FastAPI()


router = URFRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.post("/items/")
async def create_item(item: dict):
    return {"item": item}
@router.get("/file")
async def read_file():
    return FileResponse("s.xml")


@router.get("/string")
async def read_string():
    return "Hello, World!"

@router.get("/json")
async def read_json():
    raise HTTPException(status_code=400, detail="Invalid JSON payload")

app.include_router(router)


app.add_exception_handler(HTTPException,global_exception_handler)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)