import config
import random
import asyncio
from pyrogram import Client, filters

app = Client("account", api_id=config.account['api_id'], api_hash=config.account['api_hash'], session_string=config.account['session_string'])

@app.on_message(filters.text & filters.private)
async def echo(client, message):
  if message.chat.type == 'private':
    if "salam" in message.text:
      await message.reply("Salam aleykum " + message.from_user.mention)
      

app.run()
