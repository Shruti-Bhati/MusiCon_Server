from flask import Flask
app = Flask('MusiCon', template_folder= "./app/templates", static_folder='./app/static')
import routes

