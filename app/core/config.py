from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

class Settings(BaseSettings):
    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str
    RAZORPAY_WEBHOOK_SECRET: str
    GEMINI_API_KEY: str
    SERVICE_ACCOUNT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()