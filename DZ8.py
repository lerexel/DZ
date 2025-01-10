import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("simulation.log"),
        logging.StreamHandler()
    ]
)

class Human:
    def __init__(self, name='Human', job=None, car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car
        self.tire = 0
        logging.info(f"{self.name} спочатку має {self.money}$ ")

    def work(self):
        if self.job is None:
            message = f"{self.name} не має роботи, тому він лох"
            print(message)
            logging.warning(message)
            return

        self.money += self.job.salary
        self.tire += self.job.tired
        message = f"{self.name} працював і заробив {self.job.salary}$, але втомився на {self.job.tired}%"
        print(message)
        logging.info(message)

job_list = {
    "Java developer":
        {"salary": 50, "gladness_less": 10, "tired": 30},
    "Python developer":
        {"salary": 40, "gladness_less": 3, "tired": 25},
    "C++ developer":
        {"salary": 45, "gladness_less": 25, "tired": 50},
    "Content creator":
        {"salary": 39, "gladness_less": 1, "tired": 10},
}

class Job:
    def __init__(self, job_list):
        self.job_name = random.choice(list(job_list))
        self.salary = job_list[self.job_name]["salary"]
        self.tired = job_list[self.job_name]["tired"]
        logging.info(f"sasha назначений на роботу  {self.job_name} з зарплатою {self.salary}$ і втомлювастю {self.tired}%")

sasha = Human('sasha', Job(job_list))
sasha.work()

logging.info(f"{sasha.name} заробив гроші і тепер має {sasha.money}$ та втомився на {sasha.tire}%")
print(f"{sasha.name} заробив гроші і тепер має {sasha.money}$ та втомився на {sasha.tire}%")
