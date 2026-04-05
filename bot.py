import os
import asyncio
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

API_ID = 39765169
API_HASH = "f65e0f735a50751bd7d22f5ff83bde66"
SESSION_STRING = os.environ.get("SESSION_STRING")

SOURCE_CHATS = ["pubgleakchannel", "COMFYSHAHBAJ", "MadTamizha"]
TARGET_CHAT = "gemeraleakchat"
FORBIDDEN_WORDS = ["link 18+", "lừa đảo", "hack"]

if SESSION_STRING:
    app = Client("my_cipher_bot", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
else:
    app = Client("my_cipher_bot", api_id=API_ID, api_hash=API_HASH)

processed_media_hashes = set()
is_afk = False

web_server = Flask(__name__)

@web_server.route('/')
def home():
    return "Cipher Bot is ALIVE!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    web_server.run(host="0.0.0.0", port=port)

def keep_alive():
    server_thread = Thread(target=run_server)
    server_thread.start()

@app.on_message(filters.me & (filters.command("ping", prefixes=["/", "\\"]) | filters.regex(r"(?i)^ping$")))
async def handle_ping(client, message):
    status_text = "🦾 **Pong! Cipher online.**\n\nAll systems operational."
    await message.reply_text(status_text)

@app.on_message(filters.chat(SOURCE_CHATS))
async def mirror_and_scan(client, message):
    try:
        if message.media:
            file_unique_id = None
            if message.photo:
                file_unique_id = message.photo.file_unique_id
            elif message.video:
                file_unique_id = message.video.file_unique_id
            elif message.document:
                file_unique_id = message.document.file_unique_id
            
            if file_unique_id:
                if file_unique_id in processed_media_hashes:
                    return 
                processed_media_hashes.add(file_unique_id)
        
        await message.copy(TARGET_CHAT)
    except Exception:
        pass

@app.on_message(filters.me & filters.command("id", prefixes=["/", "."]))
async def get_chat_id(client, message):
    await message.reply_text(f"`{message.chat.id}`")

@app.on_message(filters.me & filters.command("help", prefixes=["/", "."]))
async def show_help(client, message):
    await message.reply_text("/ping, /id, /afk")

@app.on_message(filters.me & filters.text)
async def custom_reply(client, message):
    text_content = message.text.lower()
    if "xóa tin" in text_content:
        await message.reply_text("Processing...")

@app.on_message(filters.me & filters.command("afk", prefixes=["/", "."]))
async def toggle_afk(client, message):
    global is_afk
    is_afk = not is_afk
    status = "ON" if is_afk else "OFF"
    await message.reply_text(f"AFK: {status}")

@app.on_message(filters.private & ~filters.me)
async def afk_auto_reply(client, message):
    global is_afk
    if is_afk:
        await message.reply_text("Currently AFK. Please leave a message.")

@app.on_message(filters.chat(TARGET_CHAT))
async def auto_react_own_channel(client, message):
    try:
        await message.react(emoji="🔥")
    except Exception:
        pass

@app.on_message(filters.group & filters.text & ~filters.me)
async def auto_censor(client, message):
    text_content = message.text.lower()
    if any(word in text_content for word in FORBIDDEN_WORDS):
        try:
            await message.delete()
        except Exception:
            pass

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    keep_alive()
    app.run()
