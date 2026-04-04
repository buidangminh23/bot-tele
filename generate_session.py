import asyncio
from pyrogram import Client

API_ID = 39765169
API_HASH = "f65e0f735a50751bd7d22f5ff83bde66"

async def execute_session_generation():
    app = Client("memory_session", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await app.start()
    session_data = await app.export_session_string()
    
    print("\n\n")
    print(session_data)
    print("\n\n")
    
    await app.stop()

if __name__ == "__main__":
    asyncio.run(execute_session_generation())