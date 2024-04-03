import time
import asyncio,aiohttp

semaphore=asyncio.Semaphore(5)

async def Get(url):
    async with semaphore:
        params = {'name': 'germey', 'age': 25}
        async with aiohttp.ClientSession() as session:
            resp=await session.get(url,params=params)
            return await resp.text()

async def Request():
    url='https://httpbin.org/delay/5'
    # 2.send async request and process
    resp=await Get(url)
    print('Get response from', url, 'response', resp)

def main():
    start = time.time()
    # 1. define coroutine task and run
    tasks=[asyncio.ensure_future(Request()) for _ in range(10)]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('Cost time:', end - start)

if __name__=='__main__':
    main()