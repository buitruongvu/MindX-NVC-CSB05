def sort_colors(nums):
  count_red = nums.count('r')
  count_white = nums.count('w')
  count_blue = nums.count('b')
  sorted_balls = count_red * ['r'] + count_white * ['w'] + count_blue * ['b']
  return sorted_balls

nums = ['r', 'w', 'b', 'w', 'w', 'r', 'w', 'b']
print(sort_colors(nums))

print(2 * ['r'])
print([1, 5] + [3, 6, 9])
  