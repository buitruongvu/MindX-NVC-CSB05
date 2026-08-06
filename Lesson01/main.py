# Vòng lặp for với số lần lặp biết trước
for i in range(4): # start = 0 end=4 Tuy nhiên chỉ chạy tới 3
  print(i)
for i in range(2, 6):
  print(i)
for i in range(2, 6, 2): # start = 2, end = 6, step = 2
  print(i)
# Vòng lặp while
i = 0
while i < 5:
  print(i)
  i += 1 # i = i + 1
print(4 != 5)

n = int(input("Enter n:"))
while n != -1:
  n = int(input("Enter n again: "))
