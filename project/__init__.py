from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient


app = Flask(__name__)
from . import views
