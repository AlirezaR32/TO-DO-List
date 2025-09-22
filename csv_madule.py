import csv
from task import Task
def seve_to_csv(data):
    with open("backup.csv", "w", newline='') as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(["name, description, priority"])
            for item in data:
                csv_writer.writerow(item.details())
    
def load_from_task(tasklist):
    with open("backup.csv") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for line in csv_reader:
                if line:
                    name, description, priority = line
                    task = Task(name, description, priority)
                    tasklist.append(task)