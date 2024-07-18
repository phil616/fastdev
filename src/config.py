import warnings
from pydantic import (
    PostgresDsn,
    MySQLDsn,
    computed_field,
    model_validator,
    Field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings
from typing_extensions import Self,List,Union
from os import walk, path

# Default String  = "CHANGETHIS"
class Settings(BaseSettings):
    # ---- Project Basic Config ----
    MODEL_DIR:str = Field(default="model")
    ENVIRONMENT:str = Field(default="development")
    
    # STATIC_DIR: str = path.join(getcwd(), "static")
    # TEMPLATE_DIR: str = path.join(STATIC_DIR, "templates")
    # ---- Application Basic Config ----
    PROJECT_NAME: str = Field(default="FastDev",description="")
    APP_NAME: str = Field(default="0.0.1",description="")
    APP_DESC: str = Field(default="FastDev",description="")
    APP_VERSION: str = Field(default="0.0.1",description="")
    API_V1_STR: str = Field(default="/api/v1")
    # ---- OpenAPI -----
    LOGO_URL: str = Field(default="/logo-teal.png")
    SWAGGER_UI_OAUTH2_REDIRECT_URL: str = Field(default="/api/v1/test/oath2")
    # ---- MySQL Base ----
    MYSQL_HOST:str = Field(default="localhost")
    MYSQL_PORT:int = Field(default=3306)
    MYSQL_USER:str = Field(default="root")
    MYSQL_PASSWORD:str = Field(default="<PASSWORD>")
    MYSQL_DB:str = Field(default="app")
    MYSQL_TIMEZONE:str = Field(default="Asia/Shanghai")

    @computed_field
    @property
    def MYSQL_DB_URI(self)->MySQLDsn:
        return MultiHostUrl.build(
            scheme="mysql+pymysql",
            username=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            host=self.MYSQL_HOST,
            port=self.MYSQL_PORT,
            path=self.MYSQL_DB,
        )
    @computed_field
    @property
    def MYSQL_DB_CONFIG(self)->dict:
        skip_files = ['Basic.py', '__init__.py']
        ret = []
        for _, _, i in walk(path.join("MODEL_DIR")):
            models = list(set(i) - set(skip_files))
            for model in models:
                model = model.replace(".py", "")
                model = "models." + model
                ret.append(model)
            break

        return {
        "connections": {
            "default": {  # base database named base
                'engine': 'tortoise.backends.mysql',
                "credentials": {
                    'host': self.MYSQL_HOST,
                    'user': self.MYSQL_USER,
                    'password': self.MYSQL_PASSWORD,  # password of mysql server
                    'port': self.MYSQL_PORT,
                    'database': self.MYSQL_DB,  # name of mysql database server
                }
            },
        },
        "apps": {
            "models": {
                "models": models,  # model file in ./models
                "default_connection": "default"  # link to `base` database
            },
        },
        'use_tz': True,
        'timezone': self.MYSQL_TIMEZONE
    }

    # ---- Postgres ----

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "CHANGETHIS"
    POSTGRES_DB: str = "app"
    
    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    # ---- SMTP ----
    
    SMTP_TLS: bool = True
    SMTP_SSL: bool = False
    SMTP_PORT: int = 587
    SMTP_HOST: Union[str, None] = None
    SMTP_USER: Union[str, None] = None
    SMTP_PASSWORD: Union[str, None] = None
    # TODO: update type to EmailStr when sqlmodel supports it
    EMAILS_FROM_EMAIL: Union[str , None] = None
    EMAILS_FROM_NAME: Union[str, None] = None

    # ---- Redis ----

    
    # ---- CORS ---- # Cross-Origin Resource Sharing Policy
    CORS_ALLOW_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]

    # ---- Secure ---- # JWT (JSON Web Token)
    JWT_SECRET_KEY: str = Field(default="CHANGETHIS",env="JWT_SECRET_KEY",description="JWT密钥")
    JWT_ACCESS_EXPIRE_MINUTES: int = Field(default=24*60,env="JWT_ACCESS_EXPIRE_MINUTES",description="JWT过期时间")
    JWT_ALGORITHM: str = Field(default="HS256",env="JWT_ALGORITHM",description="JWT算法")


    # ---- Cloud Services ----

    # ---- Storage ----

    # ---- Message Queue ----

    # ---- Etcd ----

    # ---- Switches ----
    ENABLE_SYSTEM_SIGNAL:bool = Field(default=True)
    ENABLE_BACKEND_CORS_ORIGINS:bool = Field(default=True)

    # Model Secure
    def _check_default_secret(self, var_name: str, value: Union[str, None]) -> None:
        if value == "CHANGETHIS":
            message = (
                f'The value of {var_name} is "CHANGETHIS", '
                "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("JWT_SECRET_KEY", self.JWT_SECRET_KEY)
        self._check_default_secret("POSTGRES_PASSWORD", self.POSTGRES_PASSWORD)
        self._check_default_secret("SMTP_PASSWORD",self.SMTP_PASSWORD)
        self._check_default_secret("MYSQL_PASSWORD", self.MYSQL_PASSWORD)
        return self

    class Config:
        env_file = ".env"  # Path to a file containing environment variables

settings = Settings()  # type: ignore
