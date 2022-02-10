from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
#from flask_restx import Api

#api = Api()

app = Flask(__name__)#identify the current module passed to Flask
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
#api.init_app(app)

from application import routes, models