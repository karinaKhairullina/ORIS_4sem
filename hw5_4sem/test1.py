import asyncio
import aiohttp
import json


async def fetch_cats(url, session):
    async with session.get(url) as response:
        cats = await response.json()
        return cats


async def get_cats():
    async with aiohttp.ClientSession() as session:
        # Запрос на получение 10 фактов о котах
        urls = ['https://catfact.ninja/fact' for i in range(10)]
        tasks = [fetch_cats(url, session) for url in urls]
        results = await asyncio.gather(*tasks)

        # Запись результатов в файлы
        for i, result in enumerate(results):
            filename = f'file/cat_fact_{i+1}.txt'
            with open(filename, 'w') as f:
                f.write(json.dumps(result))


loop = asyncio.get_event_loop()
loop.run_until_complete(get_cats())
