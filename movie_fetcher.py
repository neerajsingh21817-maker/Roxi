# movie_fetcher.py

from pyrogram import Client
from config import API_ID, API_HASH, SESSION_NAME, DELIVERY_CHANNEL_ID

# Function to get movie file from delivery channel
async def get_movie_file(message_id):
    async with Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH) as app:
        try:
            message = await app.get_messages(chat_id=DELIVERY_CHANNEL_ID, message_ids=message_id)
            return message
        except Exception as e:
            print(f"[ERROR] Failed to fetch message: {e}")
            return None
