from app.utils.responseCode import ResponseCode
import os
from app.config import Config
import jwt
from datetime import datetime,timedelta
def httpResponse(code,message="",data={},http_code = 200):
    return {
        "status": True if code < 300 else False,
        "code" : code,
        "message" : message if message else ResponseCode.responses[code],
        "data" : data
    }, http_code if code < 400 else code 

def generateToken(user_id,is_author,exp,secret):
    return jwt.encode(
                    payload={
                        "user_id":user_id,
                        "exp":datetime.utcnow() + timedelta(seconds=int(exp)),
                        "iat":datetime.utcnow(),
                        "is_author":is_author
                    },
                    key=secret,
                    algorithm="HS256"
                )


def generateAccessToken(user_id,is_author):
    return generateToken(user_id,is_author,Config.ACCESS_TOKEN_EXP_TIME,Config.ACCESS_TOKEN_SECRET_KEY)

def generateRefreshToken(user_id,is_author):
    return generateToken(user_id,is_author,Config.REFRESH_TOKEN_EXP_TIME,Config.REFRESH_TOKEN_SECRET_KEY)
    