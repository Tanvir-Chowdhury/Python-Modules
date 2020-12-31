import aiohttp
import asyncio

'''async def make_request():
    url = "https://example.com"
    print(f"making request to {url}")
    async with aiohttp.ClientSession() as session :
        async with session.get(url) as resp:
            if resp.status == 200:
                print(await resp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())


async def make_requests():
    url = 'https://coreyms.com'
    print(f'making request from {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp)
            if resp.status == 200:
                print(await resp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(make_requests())'''



async def makiing_req(session, n_req):
    url = "https://example.com"
    print(f'making {n_req} to {url}')
    async with session.get(url) as resp:
        if resp.status == 200:
            print(await resp.text())

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[makiing_req(session, i) for i in range(10)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())