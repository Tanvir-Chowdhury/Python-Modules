import asyncio
import time

async def waiting(n):
    print(f"waiting for {n} seconds")
    await asyncio.sleep(n)

async def main():
    await asyncio.gather(*[waiting(2), waiting(5), waiting(9)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
