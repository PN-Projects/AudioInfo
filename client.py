# This bot is created by the PN-Projects kindly be wise enough to give credits while kanging 
# u can buy me a coffee at t.me/dotenv or k.parthiv@paytm 

import os
from pyrogram import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize Pyrogram client
app = Client("audio_metadata_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
