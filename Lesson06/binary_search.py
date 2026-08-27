# Bùi Quang Minh: Con cần học thêm về list, index của list, truy cập phần tử trong list
num = 7
nums_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# length(nums_sorted) = 10
# mid = 5 [0, 4] [5, 9]
# mid = nums_sorted[5 - 1] so sánh với 7: mid = nums_sorted[4] = 5 < num = 7 
# lấy khoảng sau của mid là [5, 9]
# mid mới = index = 7 thì sẽ có 2 khoảng mới [5, 6] [mid = 7] [8, 9]
# mid_new = nums_sorted[7] = 8 > num = 7 => lấy khoảng trước
# [5, 6]
# mid_mới index = 5 sẽ có 2 khoảng mới là [5] và [6]
# mid_new = nums_sorted[5] = 6 < num =7 => lấy khoảng sau [6] 
# => num = 7 => index = 6 
# Độ phức tạp của thuật toán trên là O(log2(n))

num = 7
nums_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        print(start, end)
        mid = (start+end)//2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:   # arr[mid] == target
            return mid
    return -1   # Not found