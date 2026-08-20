import math
from time import time

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

begin = time()
num = 999999937
#toán tử ba ngôi (ternary operator)
print(num, "is prime" if is_prime(num) else "is not prime")
end = time()
print("Algorithm took", end - begin, "seconds")
print("------------------------------------------")
def is_prime_optimize(n):
  if n < 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


begin = time()
num = 999999937
#toán tử ba ngôi (ternary operator)
print(num, "is prime" if is_prime_optimize(num) else "is not prime")
end = time()
print("Algorithm took", end - begin, "seconds")