# List 
numbers = [1, 2, 3, 4, 5, 6]
#Truy cập phần tử
print(numbers[3]) #output: 4
#Độ dài của list 
print(len(numbers)) #output: 6

animals = ["dog", "cat", "lion", "rabbit"]
animals[2] = "tiger"
print(animals)

mixed = [ 3, "Python", True, 4.5, 10]
del mixed[4]
print(mixed) #output: [3, 'Python', True, 4.5]

mixed.append("Nguyen Minh Tuan")
print(mixed) # output: [3, 'Python', True, 4.5, 'Nguyen Minh Tuan']
mixed.append(["Tu", "Minh", "Tan", "Duong", "Gia"]) 
#output: [3, 'Python', True, 4.5, 'Nguyen Minh Tuan', ['Tu', 'Minh', 'Tan', 'Duong', 'Gia']]
print(mixed)
#Duyệt phần tử
for animal in animals: # animals = ["dog", "cat", "lion", "rabbit"]
  print(animal)
#hoặc:
print("----------------------")
for i in range(len(animals)):
  print(animals[i])
