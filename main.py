import config
import random
import asyncio
from pyrogram import Client

async def main():
  async with Client("account", api_id=config.account['api_id'], api_hash=config.account['api_hash'], session_string=config.account['session_string']) as app:
    while True:
      bio = random.choice(config.bio)
      await app.update_profile(bio=bio)
      await asyncio.sleep(1200)

asyncio.run(main())
