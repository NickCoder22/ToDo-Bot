from database import *
import asyncio
import datetime

async def main():
    dbcfg = open("db.cfg")
    address, user, passwd, ns, db = dbcfg.readline().split()
    db = await connect(address, user, passwd, ns, db)

if __name__ == "__main__":
    asyncio.run(main())