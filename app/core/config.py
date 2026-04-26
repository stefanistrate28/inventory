# configuratia aplicatiei
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # url-ul la baza de date
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()