# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
import os
import pyrogram
import asyncio
import re
import ast
import math
import random
import pytz
import time
from datetime import datetime, timedelta, date, time
lock = asyncio.Lock()
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
import logging
logger = logging.getLogger(__name__)
from bot import channelforward
from config import Config
LOG_CHANNEL=Config.LOG_CHANNEL
from pyrogram import Client, filters
import time
from config import Config
api_id = Config.API_ID
api_hash = Config.API_HASH
my_account = Config.session_string
from time import sleep

app = Client("my_account", api_id, api_hash)

source_channel = -1001904263283  # replace with your source channel ID
destination_channel = -1002071588087 # replace with your destination channel ID
last_message_time = 0


@channelforward.on_message(filters.channel & (filters.document | filters.video | filters.photo)  & ~filters.forwarded)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
             global last_message_time
             current_time = time.time()
             if current_time - last_message_time < 5:
                 func = message.copy if Config.AS_COPY else message.forward
                 await func(int(to_channel), Config.AS_COPY)
                 await time.sleep(5)
                 last_message_time = time.time()
                 logger.info("Forwarded a message from", from_channel, "to", to_channel)
                 await asyncio.sleep(30)
   except Exception as e:
       logger.exception(e)

