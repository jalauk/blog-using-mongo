from app.models import db
from datetime import datetime

class User(db.Document):
    meta = {"collection" : "user"}
    username = db.StringField(min_length=3,max_length=64,unique=True)
    name = db.StringField(min_length=2,max_length=64)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    is_author = db.BooleanField(required=True,default=False)
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())