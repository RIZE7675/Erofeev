class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("Alice", 25)
person.display_info()

class Soda:
    def __init__(self, add=None):
        if add and isinstance(add, str) and add.isalpha():
            self.add = add
        else:
            self.add = "Обычная газировка"

    def show_my_drink(self):
        if self.add == "Обычная газировка":
            print(self.add)
        else:
            print(f"Газировка и {self.add}")



Soda().show_my_drink()
Soda('малина').show_my_drink()
Soda(5).show_my_drink()
