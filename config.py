import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB upload limit