from pyrogram import Client, filters
import time
from config import Config
api_id = Config.API_ID
api_hash = Config.API_HASH
my_account = Config.session_string
app = Client("my_account", api_id, api_hash)

source_channel = -1001904263283  # replace with your source channel ID
destination_channel = -1002102498386 # replace with your destination channel ID
last_message_time = 0

@app.on_message(filters.chat(source_channel) & ~filters.forwarded)
def forward_message(client, message):
    global last_message_time
    current_time = time.time()
    if current_time - last_message_time < 5:
        time.sleep(5)
    client.forward_messages(destination_channel, message.chat.id, [message.message_id])
    last_message_time = time.time()


