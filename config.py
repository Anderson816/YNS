import os from dotenv import load_dotenv

load_dotenv()

class Config: SECRET_KEY = os.getenv('SECRET_KEY') DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

