import os
from pyrogram import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


#init pyro client 
app = Client("audio_metadata_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
