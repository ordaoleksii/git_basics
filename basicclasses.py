class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


class Worker(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, position={self.position})"


class Company:
    def __init__(self, name, workers):
        self.name = name
        self.workers = workers

    def average_age(self):
        if not self.workers:
            return 0
        total_age = sum(worker.age for worker in self.workers)
        return total_age / len(self.workers)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, workers={self.workers})"


# Приклад використання класів
worker1 = Worker(name="John", age=30, position="Developer")
worker2 = Worker(name="Alice", age=35, position="Manager")

company = Company(name="TechCo", workers=[worker1, worker2])

print(company)
print(f"Average age of workers: {company.average_age()}")
