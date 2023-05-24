from flask import Blueprint,request
from app.services import userService
from app.schemas.userSchema import register_schema,login_schema
from app.middlewares.validatorMiddleware import validate
from app.middlewares.authMiddleware import auth

bp = Blueprint("user",__name__,url_prefix="/api/user")

@bp.post("/register")
@validate(register_schema)
def register():
    name=request.json["name"]
    email=request.json["email"]
    password=request.json["password"]
    username=request.json["username"]
    is_author=request.json["is_author"]
    return userService.register(name,email,password,username,is_author)

@bp.post("/login")
@validate(login_schema)
def login():
    email = request.json["email"]
    password = request.json["password"]
    return userService.login(email,password)

@bp.get("/profile")
@auth(True)
def profile():
    return userService.profile(request.user_id)