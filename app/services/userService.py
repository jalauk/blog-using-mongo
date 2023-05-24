from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash
from app.utils.helper import httpResponse,generateAccessToken,generateRefreshToken
from app.models.refreshToken import RefreshToken

def register(name,email,password,username,is_author):
    try:
        user = User.objects(username=username).first()
        if user:
            return  httpResponse(300)
        user = User.objects(email=email).first()
        if user:
            return  httpResponse(301)
        

        hashed_password = str(generate_password_hash(password))
        user = User(
                email=email,
                username=username,
                password=hashed_password,
                name=name,
                is_author=is_author
            )
        user.save()
        return httpResponse(201,http_code=201)
    except Exception as e:
        raise e
    
def login(email,password):
    try:
        user = User.objects(email=email).first()
        if not user:
            return httpResponse(302)
        if not check_password_hash(user.password,password):
            return httpResponse(303)
        
        access_token = generateAccessToken(str(user.id),user.is_author)
        refresh_token = generateRefreshToken(str(user.id),user.is_author)
        refresh_token = RefreshToken(user_id=user.id,refresh_token=refresh_token)
        refresh_token.save()
        data = {
            "user" : {
                "id" : str(user.id),
                "name" : user.name,
                "username" : user.username,
                "email" : user.email
            },
            "tokens" : {
                "access_token" : access_token,
                "refresh_token" : refresh_token.refresh_token
            }
        }

        return httpResponse(202,data=data)
    except Exception as e:
        raise e
    
def profile(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return httpResponse(302)
    
    data = {
        "user" : {
            "id" : str(user.id),
            "name" : user.name,
            "username" : user.username,
            "email" : user.email
        }
    }
    
    return httpResponse(200,data=data)

def resetToken(token,user_id,is_author):
    refresh_token = RefreshToken.objects(refresh_token=token)
    if refresh_token:
        access_token = generateAccessToken(user_id,is_author)
        data = {
            "access_token" : access_token
        }
        return httpResponse(203,data=data)
    return httpResponse(306)


