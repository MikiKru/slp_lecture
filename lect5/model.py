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
            f"\nstop: {self.stop_date.strftime('%Y-%m-%d')} \ncurrent status: {self.status}"
    def get_name(self):         # snake case
        return self.name

tm1 = TaskModel("Python programming", datetime(2020, 12, 31))
tm2 = TaskModel("Signal Processing", stop_date=datetime(2022, 10, 1), start_date=datetime(2022, 1, 1))
print(tm1)
print(tm2)



