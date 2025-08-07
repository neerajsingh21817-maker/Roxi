# helper.py

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Dictionary to track user steps
user_steps = {}

def save_user_step(user_id, step_data):
    user_steps[user_id] = step_data

def get_user_step(user_id):
    return user_steps.get(user_id)

def clear_user_step(user_id):
    if user_id in user_steps:
        del user_steps[user_id]

# Verification keyboard
def get_verification_keyboard(short_url, movie_code):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Verify & Get Link", url=short_url)
    ], [
        InlineKeyboardButton("🔁 I've Verified", callback_data=f"verify_done:{movie_code}")
    ]])

# Final delivery keyboard (after verification)
def get_download_keyboard():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("📥 Download Movie", callback_data="get_movie")
    ]])

# Format movie caption (optional improvement)
def format_movie_caption(title, quality, size, language, subtitle):
    return f"""
🎬 {title}
🎞 Quality: {quality}
📦 Size: {size}
🗣 Audio: {language}
🔤 Subtitles: {subtitle}
"""
