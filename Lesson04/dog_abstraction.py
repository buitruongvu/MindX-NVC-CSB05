class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        pass

class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print("Woof")

class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print("Howl")