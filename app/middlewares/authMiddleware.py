import jwt
from flask import request
from app.config import Config
from app.utils.helper import httpResponse
from app.exceptions.unauthorizedException import UnauthorizedException

def auth(check_author):
    def decorator(f):
        def wrapper(*args,**kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"]
                token = token.replace("Bearer ","")
                try:
                    payload = jwt.decode(token,Config.ACCESS_TOKEN_SECRET_KEY,algorithms=["HS256"])
                    if payload:
                        if not check_author or payload["is_author"]:
                            request.user_id = payload['user_id']
                            return f(*args, **kwargs)
                except jwt.ExpiredSignatureError:
                    return httpResponse(304)
                except jwt.InvalidTokenError:
                    return httpResponse(305)
                except Exception as e:
                    raise e
            
            raise UnauthorizedException("Token not present")
        wrapper.__name__=f.__name__
        return wrapper
    return decorator