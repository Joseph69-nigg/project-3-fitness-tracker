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
    print(f"✅ User '{name}' created with ID: {user.id}")

def list_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    print("\n--- Registered Users ---")
    for user in users:
        print(f"ID: {user.id} | Name: {user.name} | Age: {user.age}")

def log_workout():
    user_id = int(input("Enter your User ID (use option 4 to see users): "))
    user = session.get(User, user_id)
    if not user:
        print("❌ User not found.")
        return

    types = session.query(WorkoutType).all()
    print("\n--- Workout Types ---")
    for t in types:
        print(f"{t.id}: {t.name}")
    
    try:
        type_id = int(input("Select workout type ID: "))
        duration = int(input("Duration in minutes: "))
        calories = int(input("Calories burned: "))
        date_str = input("Date (YYYY-MM-DD) or leave blank for today: ")
        date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else datetime.today()

        workout = Workout(
            duration=duration,
            calories=calories,
            date=date,
            user_id=user.id,
            type_id=type_id
        )
        session.add(workout)
        session.commit()
        print("✅ Workout logged successfully!")

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers and date format.")

def view_user_workouts():
    user_id = int(input("Enter your User ID: "))
    user = session.get(User, user_id)
    if user:
        print(f"\n--- Workouts for {user.name} ---")
        for w in user.workouts:
            print(f"{w.date} - {w.type.name} - {w.duration} min - {w.calories} cal")
    else:
        print("❌ User not found.")

def main():
    init_db()
    while True:
        print("\n--- Fitness Tracker ---")
        print("1. Create User")
        print("2. Log Workout")
        print("3. View Workouts")
        print("4. List Users")  
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            create_user()
        elif choice == '2':
            log_workout()
        elif choice == '3':
            view_user_workouts()
        elif choice == '4':
            list_users()  
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()

