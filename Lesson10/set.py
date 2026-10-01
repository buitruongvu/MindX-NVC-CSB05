# Ôn tập: list (danh sách)
      # Có thể chứa các phần tử trùng lặp
      # Phần tử có thứ tự
      # Thay đổi được (mutable) 
student_name_list = ["Minh Tuấn", "Anh Tú", "Quang Minh", "Dương", "Tân", "Minh Tuấn"]
student_list_unique = set(student_name_list)
print(student_list_unique)
# Duyệt phần tử của list
# Duyệt theo chỉ số index
for i in range(len(student_name_list)):
  print(f"{i + 1}", student_name_list[i]) # f-string
print("-" * 40)
# Duyệt theo từng phần tử
i = 1
for student in student_name_list:
  print(i, student)
  i += 1
# set (Tập hợp): Là một dạng cấu trúc dữ liệu
      # Dùng để lưu trữ các phần tử không trùng lặp
      # Các phần tử không có thứ tự
# Đặc điểm của set (Tập hợp):
      # Không chứa phần tử trùng lặp
      # Phần tử không có thứ tự
      # Thay đổi được (mutable)   
# Dictionary: là cấu trúc dữ liệu dạng keys - values
student_A = {
  "name": "Duong",
  "age": 18,
}
student_B = {
  "name": "Minh",
  "age": 16
}

dict = {}

set_student_name = set()

fruit_basket = {"apple", "banana", "cherry", "apple"}
fruit_basket_unique = {"apple", "banana", "cherry", "kiwi"}
print(fruit_basket)
# print(fruit_basket_unique)
print(fruit_basket_unique)
for fruit in fruit_basket_unique:
  print(fruit)
# Thêm
fruit_basket_unique = {"apple", "banana", "cherry", "kiwi"} 
fruit_basket_unique.add("orange") # O(1)
print(fruit_basket_unique)
fruit_basket_unique.update({"peach", "watermelon"}) # O(m)
print(fruit_basket_unique)
# Xoá
fruit_basket_unique = {"apple", "banana", "cherry", "kiwi", "abv", "mnz"} 
fruit_basket_unique.remove("abv")
print(fruit_basket_unique)
fruit_basket_unique.discard("mnz")
print(fruit_basket_unique)

# Phép hợp (Union)
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak"}
meals = lunch.union(dinner) # O(n+m)
print(meals)
# or
meals = lunch | dinner
print(meals)

# Phép giao (Intersection)
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak"}

meals = lunch.intersection(dinner) #O(min(n,m))
print(meals)
# or 
meals = lunch & dinner
print(meals)

# Phép trừ (difference)
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak"}
meals_1 = lunch.difference(dinner) # O(n)
print(meals_1)
meals_2 = dinner.difference(lunch) # O(n)
print(meals_2)
# or
meals_1_copy = lunch - dinner
print(meals_1_copy)
meals_2_copy = dinner - lunch
print(meals_2_copy)








