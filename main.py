import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread

api_id = 39765169
api_hash = 'f65e0f735a50751bd7d22f5ff83bde66'
string_session = '1BVtsOKcBu0eONpjm3MGefAN1oH5ifM7i9-6KnP2K0uy9Xlf9bWOzfo_wUeIJKtLuQMPv-KRvNkZSs8_nzpflBPT6VC7Moip2FoaaKSkYcfzmX40-tmWKlIkyJGHnliX2J45igTMR-tB6CBqje91BchUfm47ORNXT3lUs8bk7wP123XzxBnr7172Tw27uKpxenrWTCQNDGcQazXfdYRvGHVUzQNWYOrBPJs18qZwfasNjebxHHfN1j_A-lyasfqS5pXMMPPePJpAcUk7T9HkrvfI_A1j5IrrzQ8Ycg_x8GxNy00Y9QRrOuMy8v7axbQrdZoOdoBpF4Du9CGS6SEfKe1aBxuMqA04='

# Đã thay tự động tên kênh nguồn và đích theo đúng ảnh của bạn
source_channels = ['PUBG - LEAKS', 'COMFY SHAHBAJ', 'Mad Tamizha']
destination_channel = 'Gemera Group'

client = TelegramClient(StringSession(string_session), api_id, api_hash)

@client.on(events.NewMessage(pattern='/ping', from_users='me'))
async def ping_handler(event):
    await event.reply('🟢 UserBot dang hoat dong 24/7!')

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    if event.message.photo or event.message.video:
        await client.send_file(destination_channel, event.message.media, caption=event.message.text or "")

app = Flask(__name__)
@app.route('/')
def home():
    return "Web ao dang chay!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    t = Thread(target=run_server)
    t.start()
    asyncio.run(main())
