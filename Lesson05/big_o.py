n = int(input()) # O(1)
s1 = 0  # O(1)

for i in range(1, n + 1): # O(n)
  s1 += i 

print(s1) # O(1)

#Độ phức tạp của toàn chương trình: O(n)

sum = 0 # O(1)
for i in range(1, n + 1): # O(n^2)
  for j in range(1, i+1):
    sum = sum + 1

print(sum) # O(1)
#Độ phức tạp của toàn chương trình: O(n^2)

# Hàm sort: O(nlogn)
# Hàm mũ pow(x, y): O(y)
# Hàm min, max: O(n)
