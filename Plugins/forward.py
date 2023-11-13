# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 

from_channel = "-1002004110207"
to_channel = "-1002110715677"

@channelforward.on_message(filters.channel)
async def forward(client, message):
    if message.chat.id == int(from_channel):
        func = message.copy if Config.AS_COPY else message.forward
        await func(int(to_channel), Config.AS_COPY)
        logger.info("Forwarded a message from", from_channel, "to", to_channel)
        await asyncio.sleep(1)
except Exception as e:
logger.exception(e)
