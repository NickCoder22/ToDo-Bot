from surrealdb import Surreal

async def create(db, chat, problem, delta):
    res = await db.create(
        'todo',
        {
            'chat': chat,
            'problem': problem,
            'delta': str(delta),
        }
    )
    return res[0]['id']

def edit(db, id, new_problem, new_delta):
    return db.query('''
    UPDATE $id MERGE {
        problem: $new_problem,
        delta: $new_delta,
    };
    ''', {
        'id': id,
        'new_problem': new_problem,
        'new_delta': str(new_delta),
    })

def remove(db, id):
    return db.delete(id)

def get_todo(db, id):
    return db.select(id)

def done(db, id):
    return db.query('''
    UPDATE $id MERGE ........0{
        done: true
    };
    ''', {
        'id': id,
    })

async def get_done_for_report(db, chat):
    res = await db.query('''
    BEGIN TRANSACTION;

    DELETE todo WHERE done = true AND done_time < time::now() - 7d;
    SELECT problem FROM todo WHERE chat = $chat AND done = true;

    COMMIT TRANSACTION;
    ''', {
        'chat': chat,
    })
    return res[0]['result']

async def get_not_done(db, chat):
    res = await db.query('''
    SELECT problem FROM todo
    WHERE chat = $chat AND done = false;
    ''', {
        'chat': chat,
    })
    return res[0]['result']

# address="ws://localhost:8000/rpc"
# database = Surreal(address)

async def connect(address,user,passwd,ns,db):
    database = Surreal(address)
    await database.connect()
    await database.signin({'user': user, 'pass': passwd})
    await database.use(ns, db)
    await database.query('''
    DEFINE FIELD done ON TABLE todo
    DEFAULT false;
    ''')
    await database.query('''
    DEFINE EVENT done_time ON TABLE todo WHEN $before.done = false AND $after.done = true THEN (
        UPDATE $after.id MERGE {
            done_time: time::now()
        }
    );
    ''')
    return database



TODO_LIST = dict()
# TODO_LIST = {
#     "todo_id": {
#         "chat_id": chat_id,
#         "problem": text,
#         "deadline": deadline,
#         "next_ping": datetime,
#         "next_ping_delta": next_ping_delta(datetime)
#     }
# }

CONFIG_CHAT = dict()
# CONFIG_CHAT = {
#     "chat_id": {
#         "stat_delta": stat_delta,
#         "next_stat": next_stat
#     }
# }

def simple_create_todo(chat_id, problem, deadline, next_ping, next_ping_delta):
    todo_id = str(chat_id) + "@" +  problem
    TODO_LIST[todo_id] = {
        "chat_id": chat_id,
        "problem": problem,
        "deadline": deadline,
        "next_ping": next_ping,
        "next_ping_delta": next_ping_delta
    }
    return todo_id

def simple_get_todo(todo_id):
    return TODO_LIST.get(todo_id, None)

def simple_remove_todo(todo_id):
    if todo_id in TODO_LIST:
        del TODO_LIST[todo_id]
    return

def simple_set_stat_freq(chat_id, stat_delta, next_stat):
    # ~next_stat += stat_delta при печати статы
    if chat_id not in CONFIG_CHAT:
        CONFIG_CHAT[chat_id] = dict()
    CONFIG_CHAT["stat_delta"] = stat_delta
    CONFIG_CHAT["next_stat"] = next_stat
    return

def simple_get_stat_freq(chat_id):
    return CONFIG_CHAT.get(chat_id, None)


def simple_get_report(chat_id, deadline):
    todo_res = dict()
    for todo_id, todo in TODO_LIST.items():
        if todo["chat_id"] == chat_id and todo["deadline"] is not None\
                and todo["deadline"] <= deadline:
            todo_res[todo_id] = todo
    return todo_res

def simple_get_report_without_deadline(chat_id):
    todo_res = {
        todo_id: todo
        for todo_id, todo in TODO_LIST.items()
        if todo["deadline"] is None
    }
    return todo_res
