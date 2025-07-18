import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['WEBHOOK_URL'] = os.getenv('DISCORD_WEBHOOK_URL')

    from .routes import main
    app.register_blueprint(main)

    return app
