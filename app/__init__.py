import os from flask import Flask from dotenv import load_dotenv

load_dotenv()

def create_app(): app = Flask(name) app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from .routes import main
app.register_blueprint(main)

return app

