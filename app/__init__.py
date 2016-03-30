from flask import Flask
from pymongo import MongoClient
app = Flask('MusiCon', template_folder= "./app/templates", static_folder='./app/static')
db = MongoClient('localhost',27017)
from models.features import features
features_collection = features().getall()
import routes