class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.type} added to the zoo"
        elif self.__budget < price:
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.type} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])

        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = sum([animal.get_needs() for animal in self.animals])

        if self.__budget < needed_money:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f'You have {len(self.animals)} animals\n'
        for type in ["Lion", "Tiger", "Cheetah"]:
            filtered = list(filter(lambda x: x.type == type, self.animals))
            result += f'----- {len(filtered)} {type}s:\n'
            for animal in filtered:
                result += f'{repr(animal)}\n'
        return result

    def workers_status(self):
        result = ""
        result += f'You have {len(self.workers)} workers\n'
        for type in ["Keeper", "Caretaker", "Vet"]:
            filtered = list(filter(lambda x: x.type == type, self.workers))
            result += f'----- {len(filtered)} {type}s:\n'
            for worker in filtered:
                result += f'{repr(worker)}\n'
        return result
