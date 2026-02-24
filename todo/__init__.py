from flask import Flask
from todo.views.routes import api  # Import the blueprint

def create_app():
    app = Flask(__name__)
    
    # Register the blueprint
    app.register_blueprint(api)
    
    return app
