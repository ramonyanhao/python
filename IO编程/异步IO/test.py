import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
print(f"started at {time.strftime('%X')}")

loop = asyncio.get_event_loop()
task=[say_after(1, 'hello'),say_after(2, 'world')]
loop.run_until_complete(asyncio.wait(task))
print(f"finished at {time.strftime('%X')}")
async def main():
    task1 = asyncio.ensure_future(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

