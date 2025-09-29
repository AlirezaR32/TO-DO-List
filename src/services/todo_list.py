from src.models.task import Task
from src.services.storage import save_to_storage, load_from_storage

class ToDoList:
    def __init__(self, tasks=[]):
        self.tasks = []  # برای جلوگیری از مشکل mutable default argument
        self.tasks.extend(tasks)

    def add_task(self, name, description, priority):
        """اضافه کردن کار جدید به لیست"""
        if not name.strip():
            raise ValueError("نام کار نمی‌تواند خالی باشد")
        task = Task(name, description, priority)
        self.tasks.append(task)
        return task

    def remove_task(self, name):
        """حذف کار با نام مشخص"""
        for i, item in enumerate(self.tasks):
            if item.name.lower() == name.lower():
                return self.tasks.pop(i)
        return None

    def get_task(self, name):
        """پیدا کردن کار با نام مشخص"""
        for task in self.tasks:
            if task.name.lower() == name.lower():
                return task
        return None

    def get_tasks_by_priority(self, priority):
        """دریافت لیست کارها بر اساس اولویت"""
        return [task for task in self.tasks if task.priority == priority]

    def update_task(self, name, description=None, priority=None):
        """به‌روزرسانی اطلاعات یک کار"""
        task = self.get_task(name)
        if task:
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            return task
        return None

    def clear_tasks(self):
        """پاک کردن تمام کارها"""
        self.tasks.clear()

    def count_tasks(self):
        """تعداد کل کارها"""
        return len(self.tasks)

    def is_empty(self):
        """آیا لیست خالی است"""
        return len(self.tasks) == 0

    def save_task(self):
        """ذخیره کارها در فایل"""
        save_to_storage(self.tasks)

    def load_tasks(self):
        """بارگذاری کارها از فایل"""
        self.clear_tasks()  # پاک کردن لیست فعلی
        load_from_storage(self.tasks)