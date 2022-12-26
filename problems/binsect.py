import bisect

nums = [1,2,5,7,8,9]

# 这两个是返回插入点

# binsect_left 能够在相同值的时候返回index
#        |
# [1, 2, 5, 7, 8, 9]
print(bisect.bisect_left(nums,5))

# binsect_left 不能
#           |
# [1, 2, 5, 7, 8, 9]
print(bisect.bisect_right(nums,5))

#           |
# [1, 2, 5, 7, 8, 9]
print(bisect.bisect_left(nums,6))
print(bisect.bisect_right(nums,6))