#Hàm đếm số lần xuất hiện của một giá trị trong danh sách
def get_frequency(ls: list, value: int):
  count = 0
  for number in ls:
    if number == value:
      count += 1
  return count

std_grades = [6, 7, 5, 8, 9, 7, 10, 8, 10, 8, 9, 6, 5, 7, 8, 6]
print(get_frequency(std_grades, 7))

#Hàm chào mừng người dùng
def greeting(username:str):
  print(f"Hello {username}!")

stdents_name = ["Tu", "Tuan", "Minh", "Duong", "Tan", "Gia"]
for student in stdents_name:
  greeting(student)
