class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def details(self):
        return [self.name, self.description, self.priority]