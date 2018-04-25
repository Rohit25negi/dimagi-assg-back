"""
learning.application
~~~~~~~~~~~~~~~~~~~~~
Module defines the flask application object. Made in the separate module to 
enable the future extension/configuration.

"""
from flask import Flask

APP = Flask(__name__)
