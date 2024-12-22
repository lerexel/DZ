#That not about me!!!

class Grandparent:
    def Kindness(self):
        print("100% kindness")


class Mom(Grandparent):
    def beauty(self):
        print("Im so beauty")

    def gender(self):
        print("Women")

class Dad:
    def power(self):
        print("Not so many power")

    def gender(self):
        print("Boy")


class Child(Dad,Mom):
    def __init__(self):
        super().beauty()
        super().power()
        print("My gender Women")

nick = Child()



























