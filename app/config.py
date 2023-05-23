import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class Config():
    DEBUG=False
    MONGODB_SETTINGS = {
        "host" : os.environ.get("MONGODB_SETTINGS")
    }
    
class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False