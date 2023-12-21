import asyncio
from bot_main import start_tg


async def main():
    await start_tg()

if __name__ == "__main__":
    asyncio.run(main())
