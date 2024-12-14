import random

class Human:

    def __init__(self, name='Human', job=None, car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car
        self.tire = 0

    def work(self):
        if self.job is None:
            print(f"{self.name} does not have a job and cannot work.")
            return

        self.money += self.job.salary
        self.tire += self.job.tired
        print(f'{self.name} worked for 8 hours and earned {self.job.salary}$.')
        print(f'{self.name} is now tired by {self.job.tired}%.')

job_list = {
"Java developer":
{"salary":50, "gladness_less": 10, "tired": 30 },
"Python developer":
{"salary":40, "gladness_less": 3, "tired": 25 },
"C++ developer":
{"salary":45, "gladness_less": 25, "tired": 50 },
"Content creator":
{"salary":39, "gladness_less": 1, "tired": 10 },
}

class Job:

    def __init__(self, job_list):
        self.job_name = random.choice(list(job_list))
        self.salary = job_list[self.job_name]["salary"]
        self.tired = job_list[self.job_name]["tired"]

class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passenger_names(self):
        print(f"Names of {self.brand} passengers: ")
        for passenger in self.passengers:
            print(passenger.name)

sasha = Human('Sasha', Job(job_list))
sasha.work()
print(f"{sasha.name} has {sasha.money}$ and is tired by {sasha.tire}%.")

