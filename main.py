import database
import asyncio

async def main():
    dbcfg = open("db.cfg")
    address, user, passwd, ns, db = dbcfg.readline().split()
    db = await database.connect(address, user, passwd, ns, db)
    print(db)


if __name__ == "__main__":
    asyncio.run(main())