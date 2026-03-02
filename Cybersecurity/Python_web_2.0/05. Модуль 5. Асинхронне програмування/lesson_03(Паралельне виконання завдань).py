# =============================================================================================
#! Паралельне виконання завдання !
# =============================================================================================

import asyncio
import random


async def random_value():
    print("start task")
    await asyncio.sleep(1)
    print("task finished")
    return random.random()


async def main():
    task = asyncio.create_task(random_value())
    print("task scheduled")
    await task
    print(f"result: {task.result()}")


if __name__ == "__main__":
    asyncio.run(main())

"""
task scheduled
start task
task finished
result: 0.6671168004203238
"""
# =============================================================================================
#! Паралельне виконання CPU-bound завдань !
# =============================================================================================
import asyncio
import concurrent.futures
from time import time


def blocks(n):
    counter = n
    start = time()
    while counter > 0:
        counter -= 1
    return time() - start


async def monitoring():
    while True:
        await asyncio.sleep(2)
        print(f"Monitoring {time()}")


async def run_blocking_tasks(executor, n):
    loop = asyncio.get_event_loop()
    print("waiting for executor tasks")
    result = await loop.run_in_executor(executor, blocks, n)
    return result


async def main():
    asyncio.create_task(monitoring())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            run_blocking_tasks(executor, n)
            for n in [50_000_000, 60_000_000, 70_000_000]
        ]
        results = await asyncio.gather(*futures)
        return results


if __name__ == "__main__":
    result = asyncio.run(main())
    for r in result:
        print(r)

"""
waiting for executor tasks
waiting for executor tasks
waiting for executor tasks
Monitoring 1771872428.9462993
Monitoring 1771872431.075876
4.438450336456299
5.132308721542358
5.255008697509766
"""
# =============================================================================================
#! Паралельне виконання IO-bound завдань !
# =============================================================================================
import requests
from time import time

urls = ["http://www.google.com", "http://www.python.org", "http://duckduckgo.com"]


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


if __name__ == "__main__":
    start = time()
    for url in urls:
        r = preview_fetch(url)
        print(r)
    print(time() - start)

"""
('http://www.google.com', '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="uk"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Ty')
('http://www.python.org', '<!doctype html>\n<html class="no-js" lang="en" dir="ltr">\n\n<head>\n    <script defer\n            file-types="bz2,chm,dmg,exe,gz,json,msi,msix,pdf,pkg,tg')
('http://duckduckgo.com', '<!DOCTYPE html><html lang="en-US" class=""><head><meta charSet="utf-8" data-next-head=""/><meta name="viewport" content="width=device-width, initial-s')
1.8531920909881592
"""
# =============================================================================================
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time

urls = ["http://www.google.com", "http://www.python.org", "http://duckduckgo.com"]


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(3) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result


if __name__ == "__main__":
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)

"""
[('http://www.google.com', '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="uk"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Ty'), ('http://www.python.org', '<!doctype html>\n<html class="no-js" lang="en" dir="ltr">\n\n<head>\n    <script defer\n            file-types="bz2,chm,dmg,exe,gz,json,msi,msix,pdf,pkg,tg'), ('http://duckduckgo.com', '<!DOCTYPE html><html lang="en-US" class=""><head><meta charSet="utf-8" data-next-head=""/><meta name="viewport" content="width=device-width, initial-s')]
0.8257074356079102
"""
# =============================================================================================
