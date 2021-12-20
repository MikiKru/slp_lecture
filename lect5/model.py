from datetime import date

# model class - determine the structure of the object
# model class - determine the structure of the data
class TaskModel:                # camel case
    def __init__(self, name, stop_date, start_date = date.today(), status = "NEW"):    # constructor / initializer
        self.name = name
        self.stop_date = stop_date
        self.start_date = start_date
        self.status = status
    def __str__(self):                                                                  # str representation of the object
        return f"task name: {self.name} \nstart: {self.start_date} \nstop: {self.stop_date} \ncurrent status: {self.status}"
    def get_name(self):         # snake case
        return self.name

tm1 = TaskModel("Python programming", "2022-02-02")
tm2 = TaskModel("Signal Processing", "2022-01-20", start_date="2022-01-01")
print(tm1)
print(tm2)



