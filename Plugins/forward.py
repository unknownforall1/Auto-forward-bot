# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config

@channelforward.on_message((filters.channel & filters.private) & (filters.document | filters.video ) , group=4)
async def private_receive_handler(Client, Message):
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
            await message.forward(chat_id=Config.BIN_CHANNEL)
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(30)
   except Exception as e:
      logger.exception(e)
    await message.forward(chat_id=Config.BIN_CHANNEL)
    logger.info("Forwarded a message from", from_channel, "to", to_channel)
    await asyncio.sleep(30)
except Exception as e:
logger.exception(e)




