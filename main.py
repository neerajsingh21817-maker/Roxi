1. main.py

from pyrogram import Client, filters from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup from config import API_ID, API_HASH, BOT_TOKEN, DELIVERY_CHANNEL from shrinkme import make_shortlink from helper import save_user_step, get_user_step import asyncio

app = Client("RoxiBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private) def start(client, message): message.reply_text( "Welcome to Roxibot!\nSend me the movie name you want.")

@app.on_message(filters.text & filters.private) def search_movie(client, message): user_id = message.from_user.id movie_name = message.text.lower()

messages = app.get_chat_history(DELIVERY_CHANNEL, limit=50)
results = []
for msg in messages:
    if msg.video and msg.caption and movie_name in msg.caption.lower():
        results.append(msg)

if not results:
    message.reply_text("Movie not found.")
    return

buttons = []
for msg in results:
    file_id = msg.video.file_id
    caption = msg.caption.split("\n")[0][:30]
    short_caption = caption if caption else "Get Movie"
    data = f"verify|{msg.id}"
    buttons.append([InlineKeyboardButton(short_caption, callback_data=data)])

reply_markup = InlineKeyboardMarkup(buttons)
message.reply_text("Select your movie:", reply_markup=reply_markup)

@app.on_callback_query() def handle_callback(client, callback_query): data = callback_query.data if data.startswith("verify"): , msg_id = data.split("|") short = make_shortlink(f"https://t.me/{client.me.username}?start=unlock{msg_id}") text = f"Please verify here first: {short}" callback_query.message.reply_text(text)

elif data.startswith("unlock"):
    pass

@app.on_message(filters.command("start") & filters.regex("unlock_")) def unlock_movie(client, message): try: msg_id = int(message.text.split("unlock_")[1]) app.copy_message(chat_id=message.chat.id, from_chat_id=DELIVERY_CHANNEL, message_id=msg_id) except: message.reply_text("Error unlocking movie.")

app.run()

