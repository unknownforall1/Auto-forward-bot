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
LOG_CHANNEL=config.LOG_CHANNEL

@channelforward.on_message(filters.channel & (filters.document | filters.video | filters.photo)  & ~filters.forwarded)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
            func = message.copy if Config.AS_COPY else message.forward
            await func(int(to_channel), Config.AS_COPY)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(30)
   except Exception as e:
      logger.exception(e)

@channelforward.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    await message.reply_text(
         text=f"<b>ʜᴇʏ {user} 😍 \n\nʏᴏᴜ ᴀʀᴇ ɴᴏᴛ Aʟʟᴏᴡᴇᴅ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇs\n ᴄʟɪᴄᴋ ʜᴇʀᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ 👇</b>"
    )
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#𝐏𝐌_𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
