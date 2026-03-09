## Find Maximum in Array
# Given an array, return the maximum value.
# Example:
# Input: [5, 7, 2, 3, 9, 8, 4]
# Output: 9

## 1
# def max_value(num):
#     maximum_value = num[0]
#     for val in num:
#         if val > maximum_value:
#             maximum_value = val
#     return maximum_value

# print(max_value([5, 7, 2, 3, 9, 8, 4]))

## 2
# def max_value(num):
#     maximum_value = num[0]
#     for val in range(1, len(num)):
#         if num[val] > maximum_value:
#             maximum_value = num[val]
#     return maximum_value

# print(max_value([5, 7, 2, 3, 9, 8, 4]))

## Built in functions

# max([5,7,2,3,9,8,4])

## Built in functions

# def max_value(num):
#     return max(num)

# print(max_value([5,7,2,3,9,8,4]))
    
    
## finding min in an array
## 1
# def minimum(num):
#     min_value = num[0]
#     for val in num:
#         if val < min_value:
#             min_value = val
#     return min_value

# print(minimum([5, 7, 2, 3, 9, 8, 4]))

## 2
def minimum(num):
    min_val = num[0]
    for val in range(1, len(num)):
        if num[val] < min_val:
            min_val = num[val]
    return min_val

print(minimum([5, 7, 1, 3, 9, 8, 4]))
    


    