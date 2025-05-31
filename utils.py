
import json
import os

DATA_FILE = 'data.json'

def load_data(filename=DATA_FILE):
    """
    Loads workout data from the specified JSON file.
    Returns a list of workout dictionaries.
    """
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data, filename=DATA_FILE):
    """
    Saves the provided list of workout dictionaries to the specified JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def filter_workouts(workouts, workout_type=None):
    """
    Filters workouts by type if specified.
    """
    if workout_type:
        return [w for w in workouts if w['workout_type'].lower() == workout_type.lower()]
    return workouts

def validate_input(prompt, cast_type=int, default=None):
    """
    Handles casting and optional default values for user input.
    """
    try:
        return cast_type(input(prompt))
    except ValueError:
        return default if default is not None else cast_type()
