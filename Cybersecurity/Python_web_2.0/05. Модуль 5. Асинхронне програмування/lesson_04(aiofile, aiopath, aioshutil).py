import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "w+") as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")


if __name__ == "__main__":
    asyncio.run(main())
# =============================================================================================
# Підхід await afp.read()
# =============================================================================================
import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "r") as afp:
        print(await afp.read())


if __name__ == "__main__":
    asyncio.run(main())

# =============================================================================================
# Підхід async for
# =============================================================================================
import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "r") as afp:
        async for line in afp:
            print(line)


if __name__ == "__main__":
    asyncio.run(main())
# =============================================================================================
import asyncio
from aiofile import AIOFile, LineReader


async def main():
    async with AIOFile("hello.txt", "r") as afp:
        async for line in LineReader(afp):
            print(line)


if __name__ == "__main__":
    asyncio.run(main())

# =============================================================================================
import asyncio
from aiopath import AsyncPath


async def main():
    apath = AsyncPath("hello.txt")
    print(await apath.exists())
    print(await apath.is_file())
    print(await apath.is_dir())


if __name__ == "__main__":
    asyncio.run(main())

"""
True
True
False
"""
# =============================================================================================
# aioshutil
# =============================================================================================
import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile


async def main():
    apath = AsyncPath("hello.txt")
    if await apath.exists():
        new_path = AsyncPath("logs")
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)


if __name__ == "__main__":
    asyncio.run(main())

# =============================================================================================
