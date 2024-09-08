# This example is from a nice little tutorial I found here:
# https://medium.com/@moraneus/mastering-pythons-asyncio-a-practical-guide-0a673265cf04
#
# It wraps a sync sleep in an async function, without using a decorator like we did in the example (async_wrapping.py)
#

import asyncio
import time


def sync_task():
    print("Starting a slow sync task...")
    time.sleep(5)  # Simulating a long task
    print("Finished the slow task.")

async def async_wrapper():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_task) # passing None makes use of the default thread pool

async def main():
    await asyncio.gather(
        async_wrapper(),
        async_wrapper(),
        # Imagine other async tasks here
    )

asyncio.run(main())

