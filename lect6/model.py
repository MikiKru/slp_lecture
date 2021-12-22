from datetime import date, datetime

# model class - determine the structure of the object
# model class - determine the structure of the data
class TaskModel:                # camel case
    def __init__(self, name, stop_date, start_date = date.today(), status = "NEW"):    # constructor / initializer
        self.name = name
        self.stop_date = stop_date
        self.start_date = start_date
        self.status = status
    def __str__(self):                                                                  # str representation of the object
        return f"task name: {self.name} \nstart: {self.start_date.strftime('%Y-%m-%d')} " \
            f"\nstop: {self.stop_date.strftime('%Y-%m-%d')} \ncurrent status: {self.status} " \
            f"\ndays to stop: {self.how_many_days_to_stop()}"
    def how_many_days_to_stop(self):
        return (self.stop_date - self.start_date).days




