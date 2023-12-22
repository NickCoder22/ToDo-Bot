from surrealdb import Surreal

async def create(db, chat, problem, deadline):
    res = await db.create(
        "todo",
        {
            "chat": chat,
            "problem": problem,
            "deadline": str(deadline),
        }
    )
    return res[0]["id"]

def edit(db, id, new_problem, new_deadline):
    return db.query("""
    UPDATE $id MERGE {
        problem: $new_problem,
        deadline: $new_deadline,
    };
    """, {
        'id': id,
        'new_problem': new_problem,
        'new_deadline': str(new_deadline),
    })

def remove(db, id):
    return db.delete(id)

def get_todo(db, id):
    return db.select(id)

def done(db, id):
    return db.query("""
    UPDATE $id MERGE {
        done: true
    };
    """, {
        'id': id,
    })

async def get_report(db, chat, first_deadline, second_deadline):
    res = await db.query("""
    SELECT id, problem, deadline, done FROM todo
        WHERE chat = $chat
        AND deadline >= $form
        AND deadline <= $to
    """, {
        'chat': chat,
        'from': str(first_deadline),
        'to': str(second_deadline),
    })
    return res[0]['result']

address="ws://localhost:8000/rpc"
database = Surreal(address)

async def connect(user,passwd,ns,db):
    await database.connect()
    await database.signin({"user": user, "pass": passwd})
    await database.use(ns, db)
    return database

