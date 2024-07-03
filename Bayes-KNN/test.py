import asyncio
import aiohttp
from time import ctime

URL = "https://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.ipynb"

async def get_api(client, url):
    async with client.get(url) as respone:
        return await respone.json()

async def fetch_hacker_news():
    async with aiohttp.ClientSession() as session:
        task1 = asyncio.create_task(get_api(session, URL))
        
        news1 = await task1 # wait till task 1 is completed
        print(f'{ctime()} {news1}')

if __name__ == "__main__":
    asyncio.run(fetch_hacker_news())