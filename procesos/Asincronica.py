import asyncio
import time

start = time.time()

async def async_sleep(a):
    await asyncio.sleep(a)

async def world(a):
    await async_sleep(a)
    print("world")

async def hello(a):
    await async_sleep(a)
    print("hello")


async def main():
    tasks = (world(2), hello(1))
    await asyncio.gather(*tasks)
    print(f"Completed after: {time.time() - start}")

asyncio.run(main())