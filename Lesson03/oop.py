# Lập trình hướng đối tượng (Object-Oriented Programming)
# Xoay quanh các dối tượng (Object)
# ----- Thuộc tính (attribute): Chỉ những đặc điểm của đối tượng
# ----- Phương thức (Method): chỉ những hành động đối tượng có thể thực hiện, hoặc thông qua phương thức có thể thay đổi được thuộc tính của dối tượng đó
# Lớp (Classes): Cho phép tạo ra các cấu trúc để mô tả đối tượng. Lớp còn được gọi là bản vẽ để tạo nên đối tượng.
class Car:
  def __init__(self, brand, color):
    self.car_brand = brand
    self.color = color
  def start(self):
    print(self.color, self.car_brand, "is starting")

car1 = Car("Vinfast", "red")
car1.start()
car2 = Car("Tesla", "white")
car2.start()

#OOP principles (Nguyên lý OOP)
# Tính đóng gói (Encapsulation means keeping data safe inside objects.) Giúp che giấu thông tin và chi tiết bên trong một đối tượng
# Tính kế thừa (Inheritance lets one class get features from another.) Cho phép một lớp (lớp con) thừa hưởng các các thuộc tính và phương thức từ lớp khác (lớp cha). Lớp con có thể tái sử dụng mã nguồn từ lớp cha, đồng thời có thể mở rộng, bổ sung thêm các thuộc tính và phương thức mới.

# Tính đa hình (Polymorphism means different classes can use the same method name in their own way.)
# Tính trừu tượng: Abstraction hides complex details and shows only what is needed.




