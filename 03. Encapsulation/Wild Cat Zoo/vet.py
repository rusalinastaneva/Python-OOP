class Vet:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Vet"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
