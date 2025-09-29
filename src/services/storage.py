import csv
from src.models.task import Task

def save_to_storage(data):
    """Save tasks to CSV file"""
    with open("data/backup.csv", "w", newline='') as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(["name", "description", "priority"])
        for item in data:
            csv_writer.writerow(item.details())

def load_from_storage(tasklist):
    """Load tasks from CSV file"""
    try:
        with open("data/backup.csv") as file:
            csv_reader = csv.reader(file)
            next(csv_reader) 

            for line in csv_reader:
                if line:
                    name, description, priority = line
                    task = Task(name, description, priority)
                    tasklist.append(task)
    except FileNotFoundError:
        # If file doesn't exist, start with empty list
        pass