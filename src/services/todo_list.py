from src.models.task import Task
from src.services.storage import save_to_storage, load_from_storage

class ToDoList:
    def __init__(self, tasks= []):
        self.tasks = tasks
        self.tasks.extend(tasks)

    def add_task(self, name, description, priority):
        if not name.strip():
            raise ValueError("نام کار نمی‌تواند خالی باشد")
        task = Task(name, description, priority)
        self.tasks.append(task)
        return task

    def remove_task(self, name):
        for i, item in enumerate(self.tasks):
            if item.name.lower() == name.lower():
                return self.tasks.pop(i)
        return None

    def get_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                return task
        return None

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def update_task(self, name, description=None, priority=None):
        task = self.get_task(name)
        if task:
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            return task
        return None

    def clear_tasks(self):
        self.tasks.clear()

    def count_tasks(self):
        return len(self.tasks)

    def is_empty(self):
        return len(self.tasks) == 0

    def save_task(self):
        save_to_storage(self.tasks)

    def load_tasks(self):
        self.clear_tasks()
        load_from_storage(self.tasks)