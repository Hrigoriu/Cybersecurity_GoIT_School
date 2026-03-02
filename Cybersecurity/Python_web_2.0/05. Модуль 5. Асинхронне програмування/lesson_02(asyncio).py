import asyncio


async def baz() -> str:
    print("Before Sleep")
    await asyncio.sleep(1)
    print("After Sleep")
    return "Hello world"


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

"""
<coroutine object baz at 0x000001F4C3B819C0>
Before Sleep
After Sleep
Hello world
"""
# =============================================================================================
from time import sleep, time

fake_users = [
    {
        "id": 1,
        "name": "April Murphy",
        "company": "Bailey Inc",
        "email": "shawnlittle@example.org",
    },
    {
        "id": 2,
        "name": "Emily Alexander",
        "company": "Martinez-Smith",
        "email": "turnerandrew@example.org",
    },
    {
        "id": 3,
        "name": "Patrick Jones",
        "company": "Young, Pruitt and Miller",
        "email": "alancoleman@example.net",
    },
]


def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    (user,) = list(filter(lambda user: user["id"] == uid, fake_users))
    return user


if __name__ == "__main__":
    start = time()
    for i in range(1, 4):
        print(get_user_sync(i))
    print(time() - start)

"""
{'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'}
{'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'}
{'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
1.502241849899292   
"""
# =============================================================================================
import asyncio
from time import time

fake_users = [
    {
        "id": 1,
        "name": "April Murphy",
        "company": "Bailey Inc",
        "email": "shawnlittle@example.org",
    },
    {
        "id": 2,
        "name": "Emily Alexander",
        "company": "Martinez-Smith",
        "email": "turnerandrew@example.org",
    },
    {
        "id": 3,
        "name": "Patrick Jones",
        "company": "Young, Pruitt and Miller",
        "email": "alancoleman@example.net",
    },
]


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    (user,) = list(filter(lambda user: user["id"] == uid, fake_users))
    return user


async def main():
    r = []
    for i in range(1, 4):
        r.append(get_user_async(i))
    return await asyncio.gather(*r)


if __name__ == "__main__":
    start = time()
    result = asyncio.run(main())
    for r in result:
        print(r)
    print(time() - start)

"""
{'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'}
{'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'}
{'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
0.5132255554199219
"""
# =============================================================================================
