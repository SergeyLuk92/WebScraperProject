from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DOMAIN_URL: str
    NUM_PAGES: int
    OUTPUT_PATH: str
    CSV_FILE_NAME: str

    class Config:
        env_file = "ParsingWebData/.env"
        env_file_encoding = "utf-8"


settings = Settings()
