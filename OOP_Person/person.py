class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


    def printPerson(self):
        print(f'{self.name} {self.age} {self.height}')
