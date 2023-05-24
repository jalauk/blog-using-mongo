from flask import Flask
from app.models import db
from flask_cors import CORS
from app.config import DevelopmentConfig
from app.utils.helper import httpResponse
from app.exceptions.accessDeniedException import AccessDeinedException
from app.exceptions.badRequestException import BadRequestException
from app.exceptions.unauthorizedException import UnauthorizedException
from app.exceptions.unprocessableEntityException import UnprocessableEntryException

app = Flask(__name__)
CORS(app)

app.config.from_object(DevelopmentConfig)

db.init_app(app)

@app.errorhandler(404)
def err_404(e):
    return httpResponse(404,"Page Not Found")

@app.errorhandler(405)
def err_405(e):
    return httpResponse(405,"Method not allowed")

@app.errorhandler(AccessDeinedException)
def accessDenied(e):
    return httpResponse(403,"Access Denied")

@app.errorhandler(UnprocessableEntryException)
def unprocessableEntry(e):
    return httpResponse(422,"Unprocessable Entity")

@app.errorhandler(UnauthorizedException)
def unauthorized(e):
    return httpResponse(401,"Unauthorized")

@app.errorhandler(Exception)
def err_500(e):
    return httpResponse(500,"Internal Server Error")
