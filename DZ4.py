class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        print(f"Сила двигуна {self.power} .")



class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def rotate_wheels(self):
        print(f" {self.wheel_count} Колеса.")



class Color:
    def __init__(self, color):
        self.color = color

    def paint(self):
        print(f"Машина пофарбована у  {self.color}.")



class Car(Engine, Wheels, Color):
    def __init__(self, power, wheel_count, color, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        Color.__init__(self, color)
        self.brand = brand

    def display_info(self):
        print(f"Бренд машини: {self.brand}")
        print(f"Сила двигуна: {self.power} HP")
        print(f"Колес у машини: {self.wheel_count}")
        print(f"Колір: {self.color}")



my_car = Car(power=200, wheel_count=4, color="чурвоний", brand="Ферарі")
my_car.start_engine()
my_car.rotate_wheels()
my_car.paint()
my_car.display_info()
