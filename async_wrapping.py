import asyncio
import time
from functools import partial, wraps


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run

@async_wrap
def sleep_async(delay):
    # there is an asyncio sleep but for our test we want to use some regular sync call here
    time.sleep(delay)
    print(f'I slept asynchronously {delay} seconds')
    return 1

async def sleep_test():
    await asyncio.gather(
        sleep_async(2),
        sleep_async(3),
        sleep_async(4),
    )
    

# @async_wrap
# def busy_loop_async():
#     j=0
#     for i in range(1,100000000):
#         j=i/2
# 
#     print(f"made cpu work hard for a few seconds j={j}...")
#     
#     return j
# 
# 
# async def cpu_test():
#     await asyncio.gather(
#        busy_loop_async(), 
#        busy_loop_async(), 
#        busy_loop_async(), 
#        busy_loop_async(), 
#        busy_loop_async(), 
#     )
#
# alternative using to_thread from asyncio itself:
# def blocking_io():
#     time.sleep(1)
# 
# async def main():
#     asyncio.to_thread(blocking_io)
# 
# asyncio.run(main())

def main():
    asyncio.run(sleep_test())
    # asyncio.run(cpu_test())


if __name__ == '__main__':
    main()


# time python async_wrapping.py 
# I slept asynchronously 2 seconds
# I slept asynchronously 3 seconds
# I slept asynchronously 4 seconds
# python async_wrapping.py  0.08s user 0.02s system 2% cpu 4.100 total

# we see our async wrapping is succesful because when we run it it only
# takes 4.1 sec instead of 9 seconds when you would run it synchronously...


