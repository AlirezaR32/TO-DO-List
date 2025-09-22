
from csv_madule import seve_to_csv,load_from_task
from task import Task

class ToDoList:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.tasks.append(task)

    def remove_task(self, name):
        for item in self.tasks:
            if item.name == name:
                self.tasks.remove(item)

    def show_list(self):
        for item in self.tasks:
            print(item.details())

    def save_task(self):
        seve_to_csv(self.tasks)

    def load_tasks(self):
        load_from_task(self.tasks)
