"""
learning.application_vars
~~~~~~~~~~~~~~~~~~~~~~
Modules defines the Applocation variable/extension used in the application



"""
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from learning.application import APP


API = Api(app=APP)
DB = SQLAlchemy(app=APP)
CORS(APP)
JWT_MANAGER = JWTManager(app=APP)
