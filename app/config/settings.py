from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    DOLARSI: str = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

    DEBUG: bool = False

    PROJECT_NAME: str = "Banza"
    PROJECT_VERSION: str = "0.1.0"

    BACKEND_CORS_ORIGINS: str = "http://127.0.0.1:8000"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True


settings = Settings()
