def selection_sort(arr:list):
  sorted = []
  while arr: #Truthy / Falsy
    miximun = min(arr)
    sorted.append(miximun)
    arr.remove(miximun)
  return sorted

lst = [12, 3, 22, 4, 0, 13]
lst_sorted = selection_sort(lst)
print(lst_sorted)



    
    
