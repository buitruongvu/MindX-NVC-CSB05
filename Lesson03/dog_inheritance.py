# dog.py
class Dog:
    tail = "long"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sound = "Woof"
        
    def get_description(self):
        return f"{self.name} is {self.age}-year-old"
        
    def speak(self):
        return self.__sound


class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)