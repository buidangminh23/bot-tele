from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Thông tin API của bạn đã được thay tự động
api_id = 39765169
api_hash = 'f65e0f735a50751bd7d22f5ff83bde66'

print("Đang khởi động tiến trình lấy String Session...")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n--- STRING SESSION CỦA BẠN LÀ ---")
    print(client.session.save())
    print("---------------------------------")
    print("Hãy copy toàn bộ đoạn mã dài ngoằng ở trên và cất đi nhé!")
