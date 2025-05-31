from db import session, init_db
from db.models import User, WorkoutType

init_db()

if not session.query(WorkoutType).first():
    types = ['Running', 'Yoga', 'Cycling']
    for t in types:
        session.add(WorkoutType(name=t))
    session.commit()
