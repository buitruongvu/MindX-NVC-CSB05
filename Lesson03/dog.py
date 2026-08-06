#Tính đóng gói (Encapsulation)
class Dog:
  def __init__(self, id, name, age, sound):
    self.__id = id # Private
    self.name = name
    self.age = age
    self._sound = sound #Protected

dog1 = Dog(113, "Bella", 1, "gau gau")
print(dog1.name)
dog1.name = "Lucy"
print(dog1.name)
print(dog1._sound)
dog1._sound = "Woof Woof"
print(dog1._sound)
# print(dog1.__id) do là thuộc tính Private nên không thể truy cập được
