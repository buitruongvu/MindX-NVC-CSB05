class Item:
  def __init__(self, quantity, price):
    self.quantity = quantity
    self.price = price

class Oder:
  def __init__(self, item_list, customer_id):
    self.item_list = item_list
    self.customer_id = customer_id
  def total(self):
    total = sum(item.price * item.quantity for item in self.item_list)
    return total
class Promo:
  def __init__(self, price, discount_rate):
    self.price = price
    self.discount_rate = discount_rate
  def discount(self):
    return self.price * (1 - self.discount_rate)
# Creating individual items
item1 = Item(quantity=2, price=10.50)
item2 = Item(quantity=5, price=4.00)
item3 = Item(quantity=1, price=50.00)
# Grouping them into a list
my_items = [item1, item2, item3]
oder1 = Oder(my_items, 112)
print(oder1.total())