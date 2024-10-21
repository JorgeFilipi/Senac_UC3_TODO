import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_AME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    PASSWORD = os.getenv('PASSWORD')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'Treu'
    DEBUG = os.getenv('DEBUG', 'False') == 'Treu'