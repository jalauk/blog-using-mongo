from flask import Flask
from app.models import db
from flask_cors import CORS
from app.config import DevelopmentConfig

app = Flask(__name__)
CORS(app)

app.config.from_object(DevelopmentConfig)

db.init_app(app)
