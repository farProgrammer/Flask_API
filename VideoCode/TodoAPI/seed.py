from models import db, connect_db, Todo
from app import app

db.drop_all()
db.create_all()

todos = [
    Todo(title="JAva is a backend language"),
    Todo(title="Python is amazing just like english language "),
    Todo(title="Javascript a part of web-development ", done=True),
    Todo(title="Start web learning with HTML!"),
    Todo(title="Stylesheet are done with CSS!", done=True),
    Todo(title="Here is the journey of web learning (backend,frontend)")
]
db.session.add_all(todos)
db.session.commit()
