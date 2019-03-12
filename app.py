# In this program we will create our Flask App and instruct it to use the 
# configuration vlues specified in the config module.

from flask import Flask
from sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

