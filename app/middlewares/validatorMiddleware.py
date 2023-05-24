from flask import request
from app.exceptions.unprocessableEntityException import UnprocessableEntryException

def validate(schema,location="body"):
    def decorator(f):
        def wrapper(*args,**kwargs):
            print("working")
            inputs = {}
            if location == "body":
                inputs = request.get_json()
            if location == "query_string":
                inputs = request.args.to_dict()
            if location == "form":
                inputs = request.form.to_dict()
            
            errors = schema.validate(inputs)
            if errors:
                errorResponse = {}
                for key in errors.keys():
                    errorResponse[key] = errors[key][0]
                
                raise UnprocessableEntryException(errorResponse)
            
            return f(*args,**kwargs)
        wrapper.__name__=f.__name__
        return wrapper
    return decorator