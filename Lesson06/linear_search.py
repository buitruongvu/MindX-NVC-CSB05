def linear_search(arr, num):
  for i in range(len(arr)): # Duyệt cho i chạy từ 0 đến len(arr) - 1 vì không lấy giá trị end
    if arr[i] == num: 
      # arr[i]: Truy cập phần tử có index = i của mảng arr
      return i
  return False

# index:0, 1, 2,  3,  4,  5, 6,  7,  8, 9, 10
nums = [4, 8, 15, 16, 23, 1, 42, 5, 47, 1, 59]
# length = len(nums) = 11 
# Example: range(5) == range(0, 5, 1) <=> (0, 1, 2, 3, 4)
     #                 range(start, end, step) Không lấy giá trị end
# range(length) = (0, 1, 2,..., 10)
print(linear_search(nums, 23)) # output: 4
print(linear_search(nums, 1)) # output: 5
# Các kiểu dữ liệu (Data type)
    # int: Số nguyên Example: 3, 4, 15, -34...
    # float: Số Thực: 12.1, 3.3, -2.0,...
    # str: Chuỗi: "Python", 'Hello World'
    # bool: Boolean: True, False
print(linear_search(nums, 105)) # output: False

# Độ phức tạp của thuật toán trên là O(n)




