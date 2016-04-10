from flask import Flask
from app.urls import create_restful_app

app = Flask(__name__)
create_restful_app(app)
