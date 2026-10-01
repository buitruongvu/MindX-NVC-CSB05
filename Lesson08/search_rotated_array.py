# Bài 3 (Mức độ Khó): Tìm kiếm Nhị phân trên Mảng xoay vòng
# Tên bài toán: Tìm kiếm phần tử trong mảng xoay vòng (Rotated Sorted Array).
# Mô tả:
# Bạn được cung cấp một mảng số nguyên nums không có phần tử trùng lặp. Mảng này ban
# đầu được sắp xếp tăng dần, nhưng sau đó bị "xoay" tại một vị trí ngẫu nhiên không báo
# trước. (Ví dụ: Mảng ban đầu [0,1,2,4,5,6,7] có thể bị xoay thành [4,5,6,7,0,1,2] ).
# Cho một số nguyên target , hãy viết hàm search_rotated_array(nums, target) để trả
# về index của target trong mảng hiện tại. Nếu target không tồn tại, trả về -1 .
# •
# • 
# Yêu cầu kỹ thuật:
# Thuật toán phải đạt độ phức tạp thời gian O(log N).
# Điều này đòi hỏi bạn phải biến đổi logic của thuật toán Tìm kiếm nhị phân (Binary
# Search) truyền thống để phát hiện xem nửa nào của mảng đang được sắp xếp đúng
# thứ tự.
# Test case tham khảo:
# 1. Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#  Output mong đợi: 4
# 2. Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
#  Output mong đợi: -1

# Binary search
def search_rotated_array(nums, target):
  left, right = 0, len(nums) - 1
  # nums = [14, 15, 25, 28, 2, 4, 6, 8, 11, 12] | target = 25 |mid = (left + right) // 2 |  mid = 6 | nums[6] = 2 |
  while left <= right:
    mid = (left + right ) // 2
    if target == nums[mid]:
      return mid
    # Kiểm tra bên nào đã sắp xếp
    if nums[left] > nums[mid]:
      # Kiểm tra target có nằm trong mảng đã sắp xếp hay không
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1      
    else:
      if nums[left] <= target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
  return -1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated_array(nums, target))

        
        
    
  