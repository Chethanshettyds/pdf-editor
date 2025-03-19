import os

class Config:
    # General Flask Config
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DEBUG = True
    
    # File Upload Config
    UPLOAD_FOLDER = "uploads"
    PROCESSED_FOLDER = "processed"
    ALLOWED_EXTENSIONS = {"pdf"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB file size limit
