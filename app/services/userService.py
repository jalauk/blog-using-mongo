from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash
from app.utils.helper import httpResponse

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
    
# def login(email,password):
#     try:
#         user = User.objects(email=email).first()
#         if not user:
#             return httpResponse(302)
#         if not check_password_hash(user.password,password):
#             return httpResponse(303)
        
        
#     except Exception as e:
#         raise e
    


