# controller classes implement logic of our application based on model classes
from datetime import date
from lect5.model import TaskModel

class TaskController:
    def __init__(self):
        self.tasks = []
    def create_task(self, name, stop_date, start_date = date.today(), status = "NEW"):
        tm = TaskModel(name, stop_date, start_date, status)
        self.tasks.append(tm)
    def print_tasks(self):
        for task in self.tasks:
            print(task)
    def find_task_by_index(self, index):
        return self.tasks[index]
    def save_tasks_to_file(self, path):
        # context manager -> embedded method looks after that file is closed
        with open(path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(str(task) + '\n')
        print(f"Data saved to file: {path}")
    def read_data_from_file(self, path):
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                print(line.strip())

tc = TaskController()
tc.create_task("T1", start_date=date(2020, 12, 1), stop_date=date(2021,2,2))
tc.create_task("T2", stop_date=date(2022,2,2))
tc.create_task("T3", start_date=date(2021, 1, 1), stop_date=date(2022,2,2), status="IN PROGRESS")
tc.print_tasks()
print("Found task: ", tc.find_task_by_index(1))
tc.save_tasks_to_file("tasks.txt")
tc.save_tasks_to_file(r'C:\Users\PROXIMO\PycharmProjects\slp_lecture\t.txt')
tc.read_data_from_file("tasks.txt")
