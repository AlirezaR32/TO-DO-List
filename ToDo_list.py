import csv


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def details(self):
        return [self.name, self.description, self.priority]


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
        with open("backup.csv", "w") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(["name, description, priority"])
            for item in self.tasks:
                csv_writer.writerow(item.details())

    def load_tasks(self):
        with open("backup.csv") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for line in csv_reader:
                if line:
                    name, description, priority = line
                    task = Task(name, description, priority)
                    self.tasks.append(task)


# ui
flag = True
while flag:
    print("TODO  LIST")
    print("----------------------------")
    user_tlist = ToDoList()
    choice = input(
        "1. Add new task \n 2. remove task \n 3. Save task to storage \n 4. Load task from \
    storage \n 5. Show list of tasks \n 6. exit \n"
    )

    if choice == "1":
        name, description, priority = input("Enter informaiton of ypur task (three value)").split()
        user_tlist.add_task(name, description, priority)
    elif choice == "2":
        name = input("Enter name of task you want delete")
        user_tlist.remove_task(name)
    elif choice == "3":
        user_tlist.save_task()
        print("task saved successfully")
    elif choice == "4":
        user_tlist.load_tasks()
        print("task loaded successfully")
    elif choice == "5":
        user_tlist.show_list()
    elif choice == "6":
        res = input("Do you want save yout task ? (y/n)")
        if res.lower() == "y":
            user_tlist.load_tasks()
        flag = False
