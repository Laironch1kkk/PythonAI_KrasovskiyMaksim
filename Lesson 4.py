# class Human:
#     height = 170
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# h = Human()
# s = Student()
# w = Worker()
#
# print(h.height)
# print("*"*20)
# print(s.height)
# print(w.satiety)
# print("*"*20)
# print(w.satiety)
# print(w.height)

class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(f"height = {self.height}")
        print(f"satiety = {self.satiety}")
        print(f"age = {self.age}")

nich = Child()


class Hello:
    def __init__(self):
        print("Hello")

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World")

hw = HelloWorld()

class Computer:
    def __init__(self, model, *args, **keywards):
    super __init__(*args, **keywards)
    self.model = model
    self.memory = 128
    def calculate(self):
        print("Calculating...")

class Computer:
    def diaplay(self):
        print("I diaplay the image on the screen..."

class SmartPhone(Computer, Dispaly):
    def print_info(self):
        print(self.diaplay())
        print(self.calculate())
        print(self.model)
        print(self.resoulution)
        print(self.memory)

so = SmartPhone
sp.print_info()

