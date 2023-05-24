from flask import Flask
from app.models import db
from flask_cors import CORS
from app.config import DevelopmentConfig
from app.utils.helper import httpResponse
from app.exceptions.accessDeniedException import AccessDeinedException
from app.exceptions.badRequestException import BadRequestException
from app.exceptions.unauthorizedException import UnauthorizedException
from app.exceptions.unprocessableEntityException import UnprocessableEntryException
from app.utils.logger import Logger
from app.controllers import userController

app = Flask(__name__)
CORS(app)

app.config.from_object(DevelopmentConfig)

db.init_app(app)

app.register_blueprint(userController.bp)

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
    return httpResponse(422,"Unprocessable Entity",e.errors)

@app.errorhandler(UnauthorizedException)
def unauthorized(e):
    return httpResponse(401,"Unauthorized",e.errors)

@app.errorhandler(BadRequestException)
def unauthorized(e):
    return httpResponse(400,"Bad Request")

@app.errorhandler(Exception)
def err_500(e):
    Logger.errorLogs(e)
    print(e)
    return httpResponse(500,"Internal Server Error")