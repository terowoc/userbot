import config
import random
import asyncio
import logging
from pyrogram import Client

logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(message)s | %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')

async def main():
    try:
        async with Client("account", api_id=config.account['api_id'], api_hash=config.account['api_hash'], session_string=config.account['session_string']) as app:
        	await app.update_profile(bio=random.choice(config.bio))
        	logging.info('Profile description updated!')
        	
    except Exception as e:
        logging.error(e)
                

asyncio.run(main())