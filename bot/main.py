# This bot is created by the PN-Projects kindly be wise enough to give credits while kanging 
# u can buy me a coffee at t.me/dotenv or k.parthiv@paytm 


import os
import asyncio
from pyrogram import filters
from bot.client import app
from mutagen import File
from pydub.utils import mediainfo
from pyrogram.types import Message

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text('Hi! Send me an audio file, and I will return its metadata.')

@app.on_message(filters.audio & filters.private)
async def audio_handler(client, message: Message):
    try:
        # Download the audio file
        audio = message.audio
        file_path = await message.download()

        # Use Mutagen to extract metadata
        audio_file = File(file_path)
        if not audio_file:
            raise ValueError("File is not a valid audio file")

        # Extract additional information using mediainfo
        audio_info = mediainfo(file_path)

        # Extracting metadata
        name = audio_file.get('TIT2', 'Unknown') if audio_file else 'Unknown'
        album = audio_file.get('TALB', 'Unknown') if audio_file else 'Unknown'
        artist = audio_file.get('TPE1', 'Unknown') if audio_file else 'Unknown'
        size = os.path.getsize(file_path) / 1024  # Size in KB
        codec = audio_info.get('codec_name', 'Unknown')
        bit_rate = audio_info.get('bit_rate', 'Unknown')
        bit_depth = audio_info.get('bits_per_raw_sample', 'Unknown')
        sampling_rate = audio_info.get('sample_rate', 'Unknown')
        channels = 'Stereo' if audio_info.get('channels', '2') == '2' else 'Mono'

        # Creating a response
        response = (
            f"Name: {name}\n"
            f"Album: {album}\n"
            f"Artist: {artist}\n"
            f"Size: {size:.2f} KB\n"
            f"Codec: {codec}\n"
            f"Bit Rate: {bit_rate}\n"
            f"Bit Depth: {bit_depth}\n"
            f"Sampling Rate: {sampling_rate} Hz\n"
            f"Channels: {channels}"
        )

        await message.reply_text(response)

    except Exception as e:
        # Handle non-audio files or other errors
        await message.reply_text("Error: Could not process the file. Please make sure to send an audio file.")
        print(f"Error: {e}")

    finally:
        # Cleanup: Delete the file after processing
        if os.path.exists(file_path):
            os.remove(file_path)

@app.on_message(filters.document & filters.private)
async def document_handler(client, message: Message):
    try:
        # If the file is not audio, notify the user and delete the file
        await message.reply_text("Please send audio files only.")
        file_path = await message.download()
    except Exception as e:
        print(f"Error handling document: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
