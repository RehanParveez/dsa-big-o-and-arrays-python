## Reverse Array 
# Example:
# Input: [2,4,6,8,10]
# Output: [10,8,6,4,2]

## 1
# def rev_arr(num):
#     left = 0
#     right = len(num) - 1
#     while left < right:
#         num[left], num[right] = num[right], num[left]
#         left += 1
#         right -= 1
#     return num

# print(rev_arr([2,4,6,8,10]))

## 2
# def rev_arr(num):
#     left = 0
#     n = len(num)
#     while left < n // 2:
#         num[left], num[n - 1 - left] = num[n - 1 - left], num[left]
#         left += 1
#     return num

# print(rev_arr([2,4,6,8,10]))