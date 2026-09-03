def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)- i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

lst = [12, 3, 22, 4, 0, 13]
print(bubble_sort(lst))