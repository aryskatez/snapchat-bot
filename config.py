import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    PORT = int(os.getenv('PORT', 5000))
    
    # Snapchat
    SNAPCHAT_API_TOKEN = os.getenv('SNAPCHAT_API_TOKEN')
    SNAPCHAT_API_URL = os.getenv('SNAPCHAT_API_URL', 'https://api.snapchat.com/v1')
    
    # AI Service
    AI_SERVICE = os.getenv('AI_SERVICE', 'openai')  # 'openai' or 'gemini'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Validation
    @classmethod
    def validate(cls):
        if not cls.SNAPCHAT_API_TOKEN:
            print('Warning: SNAPCHAT_API_TOKEN not set')
        if cls.AI_SERVICE == 'openai' and not cls.OPENAI_API_KEY:
            print('Warning: OPENAI_API_KEY not set')
        if cls.AI_SERVICE == 'gemini' and not cls.GEMINI_API_KEY:
            print('Warning: GEMINI_API_KEY not set')
