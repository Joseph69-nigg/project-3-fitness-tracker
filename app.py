
from models import Workout
from utils import load_data, save_data, filter_workouts
from datetime import datetime

def log_workout():
    """
    Handles input for logging a new workout and saving it.
    """
    workout_type = input("Enter workout type (e.g., running, yoga): ").strip()
    try:
        duration = int(input("Enter duration (in minutes): "))
        calories = int(input("Enter calories burned: "))
    except ValueError:
        print("Invalid input. Duration and calories must be numbers.")
        return

    date_input = input("Enter date (YYYY-MM-DD) or press enter for today: ").strip()
    date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

    workout = Workout(workout_type, duration, calories, date)
    data = load_data()
    data.append(workout.to_dict())
    save_data(data)
    print("✅ Workout logged successfully!")

def view_workouts():
    """
    Displays all workouts, optionally filtered by type.
    """
    data = load_data()
    if not data:
        print("No workouts found.")
        return

    workout_type = input("Enter workout type to filter by (or press enter to view all): ").strip()
    filtered = filter_workouts(data, workout_type)

    if not filtered:
        print("No matching workouts found.")
        return

    for idx, w in enumerate(filtered, start=1):
        print(f"\nWorkout {idx}:")
        print(f" Type: {w['workout_type']}")
        print(f" Duration: {w['duration']} minutes")
        print(f" Calories: {w['calories']} kcal")
        print(f" Date: {w['date']}")

def main_menu():
    """
    Main loop for the application menu.
    """
    while True:
        print("\n--- Fitness Tracker ---")
        print("1. Log Workout")
        print("2. View Workouts")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            log_workout()
        elif choice == '2':
            view_workouts()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
