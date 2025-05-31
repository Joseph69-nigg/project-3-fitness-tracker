from db import session, init_db
from db.models import User, Workout, WorkoutType
from datetime import datetime

def create_user():
    name = input("Name: ")
    age = int(input("Age: "))
    weight = int(input("Weight (kg): "))
    height = int(input("Height (cm): "))
    user = User(name=name, age=age, weight=weight, height=height)
    session.add(user)
    session.commit()
    print(f"User {name} created!")

def log_workout():
    user_id = int(input("Enter your User ID: "))
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return

    types = session.query(WorkoutType).all()
    for t in types:
        print(f"{t.id}: {t.name}")
    type_id = int(input("Select workout type ID: "))
    duration = int(input("Duration in minutes: "))
    calories = int(input("Calories burned: "))
    date = input("Date (YYYY-MM-DD): ")
    workout = Workout(
        duration=duration,
        calories=calories,
        date=datetime.strptime(date, "%Y-%m-%d"),
        user_id=user.id,
        type_id=type_id
    )
    session.add(workout)
    session.commit()
    print("Workout logged!")

def view_user_workouts():
    user_id = int(input("Enter your User ID: "))
    user = session.get(User, user_id)
    if user:
        for w in user.workouts:
            print(f"{w.date} - {w.type.name} - {w.duration} min - {w.calories} cal")
    else:
        print("User not found.")

def main():
    init_db()
    while True:
        print("\n1. Create User\n2. Log Workout\n3. View Workouts\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_user()
        elif choice == '2':
            log_workout()
        elif choice == '3':
            view_user_workouts()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
