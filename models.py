class Workout:
    """
    Represents a fitness workout session.
    """
    def __init__(self, workout_type, duration, calories, date):
        self.workout_type = workout_type
        self.duration = duration  
        self.calories = calories
        self.date = date  

    def to_dict(self):
        """
        Converts the Workout instance into a dictionary.
        """
        return {
            "workout_type": self.workout_type,
            "duration": self.duration,
            "calories": self.calories,
            "date": self.date
        }