# app/__init__.py
from flask import Flask
from app.mkad_distance_calculator.routes import MDCalculator

def create_app():
    app = Flask(__name__)

    app.register_blueprint(MDCalculator)

    return app
