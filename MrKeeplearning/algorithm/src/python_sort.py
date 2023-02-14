# 파이썬 sort()
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr.sort()

print(arr)
# Output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr.sort(reverse=True)

print(arr)
# Output is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 파이썬 sorted()
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorted_arr = sorted(arr)

print(sorted_arr)
# Output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse_sorted_arr = sorted(arr, reverse=True)
print(reverse_sorted_arr)
# Output is [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
