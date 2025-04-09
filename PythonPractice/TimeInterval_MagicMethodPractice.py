
"""
Class to practice magic methods: multiplication, addition, and string
"""

class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def get_hours_unit(time_in_seconds):
        return time_in_seconds // 3600
    def get_minutes_unit(time_in_seconds):
        return (time_in_seconds % 3600) // 60
    def get_seconds_unit(time_in_seconds):
        return ((time_in_seconds % 3600) % 60)
    def get_full_seconds(aTimeInterval):
        if not isinstance(aTimeInterval, TimeInterval):
            raise TypeError("argument is the wrong type")
        return ((aTimeInterval.hours * 3600) + (aTimeInterval.minutes * 60) 
        + (aTimeInterval.seconds))
    def get_time_interval_from_seconds(new_full_seconds):
        new_hours = TimeInterval.get_hours_unit(new_full_seconds)
        new_minutes = TimeInterval.get_minutes_unit(new_full_seconds)
        new_seconds = TimeInterval.get_seconds_unit(new_full_seconds)
        return TimeInterval(new_hours, new_minutes, new_seconds)

    def __mul__(self, val):
        curr_full_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds 
        new_full_seconds = curr_full_seconds * val
        
        return TimeInterval.get_time_interval_from_seconds(new_full_seconds)
    def __add__(self, otherTimeInterval):
        if not isinstance(otherTimeInterval, TimeInterval):
            raise TypeError("argument is the wrong type")
        return TimeInterval.get_time_interval_from_seconds(TimeInterval.get_full_seconds(self) + 
        TimeInterval.get_full_seconds(otherTimeInterval))
        
    def __str__(self):
        return f"{self.hours}h; {self.minutes}m; {self.seconds}s"

if __name__ == "__main__":
    my_time = TimeInterval(1, 55, 23)
    print(my_time + TimeInterval(4, 0, 0))
    print(TimeInterval.get_full_seconds(my_time))
