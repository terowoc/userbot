import config
from pyrogram import Client

async def main():
        try:
            async with Client("account", api_id=config.account['api_id'], api_hash=config.account['api_hash'], session_string=config.account['session_string']) as app:
            	
        except Exception as e:
        	print(e)
                

asyncio.run(main())