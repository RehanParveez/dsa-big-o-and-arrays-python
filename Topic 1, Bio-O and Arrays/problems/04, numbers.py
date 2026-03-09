## adding all elements
# def sum_num(num):
#     answer = 0
#     for val in num:
#         answer = answer + val
#     return answer

# print(sum_num([1, 2, 3, 4, 6, 7, 8, 9, 5]))


## even numbers count in array

# def even(num):
#     count = 0
#     for val in num:
#         if val % 2 == 0:
#             count += 1
#     return count
# print(even([1, 2, 3, 4, 6, 7, 8, 9, 5]))


## average finding of the array elements
## 1
# def avg(num):
#     answer = 0
#     for val in num:
#         answer = answer + val
#     average = answer / len(num)
#     return average

# print(avg([1, 2, 3, 4, 6, 7, 8, 9, 5]))

## 2
# def avg(num):
#     answer = 0
#     full = len(num)
#     for val in num:
#         answer = answer + (val / full)
#     return answer

# print(avg([1, 2, 3, 4, 6, 7, 8, 9, 5]))


# index finding of an elment
# def element(num, target):
#     position = 0
#     for val in num:
#         if val == target:
#             return position
#         position += 1
#     return -1

# print(element([5,7,2,3,9,8,4], 8))


## all zeros to be moved to the End
# def move(num):
#     non_zero = []
#     zeros = []
#     for val in num:
#         if val == 0:
#             zeros.append(val)
#         else:
#             non_zero.append(val)
#     return non_zero + zeros

# print(move([6,0,2,0,9,0,1]))
        
        
## second largest number in an array
## 1
# def find(num):
#     largest = num[0]
#     for val in num:
#         if val > largest:
#             largest = val
#     num.remove(largest)
    
#     second_largest = num[0]
#     for val in num:
#         if val > second_largest:
#             second_largest = val
#     return second_largest

# print(find([5,7,2,3,9,8,4]))

## 2
# def find(num):
#     largest = num[0]
#     second_largest = num[0]
#     for val in num:
#         if val > largest:
#             second_largest = largest
#             largest = val
#         elif val > second_largest and val != largest:
#             second_largest = val
#     return second_largest

# print(find([5,7,2,3,9,8,4]))


## removing duplicates from array
## 1
# def duplicate(num):
#     nums = []
#     for val in num:
#         found = False
#         for v in nums:
#             if v == val:
#                 found = True
#         if found == False:
#             nums.append(val)
#     return nums

# print(duplicate([1,2,2,3,4,4,5]))

## 2
# def duplicate(num):
#     result = []
#     for val in num:
#         if val not in result:
#             result.append(val)
#     return result
 
# print(duplicate([1,2,2,3,4,4,5]))


## finding the missing number
## 1
# def missing(nums):
#     val = 1
#     while True:
#        count = 0
#        for v in nums:
#           if v == val:
#              count = count + 1
#           if count == 0:
#             return val
#        val += 1

# print(missing([2,3,4,5,6,8,9]))

## 2 
# def missing(nums):
#     largest = nums[0]
#     for val in nums:
#        if val > largest:
#           largest = val
#     for v in range(1, largest + 1):
#        if v not in nums:
#           return v

# print(missing([2,3,4,5,6,8,9]))


## finding the pairs that have sum same as target
# ## 1
# def pairs(num, target):
#     val = 0
#     while val < len(num):
#         v = 0
#         while v < len(num):
#             if val != v:
#               if num[val] + num[v] == target:
#                 print(num[val], num[v])
#             v += 1
#         val += 1

# pairs([2,4,3,5,7,8], 9)

# ##2
# def pairs(num, target):
#     for val in range(len(num)):
#        for v in range(val + 1, len(num)):
#           if num[val] + num[v] == target:
#             print(num[val], num[v])

# print(pairs([2,4,3,5,7,8], 9))


## rotating the array by one position
## 1
# def rotate(nums):
#     num = []
#     last = nums[len(nums)]
#     num.append(last)
#     val = 0
#     while val < len(nums):
#         num.append(nums[val])
#         val += 1
#     return num
#
# print(rotate([4,2,5,9,7]))

## 2
# def rotate(nums):
#     last = nums[len(nums) - 1]
#     num = len(nums) - 1
#     while num > 0:
#         nums[num] = nums[num - 1]
#         num -= 1
#     nums[0] = last
#     return nums

# print(rotate([4,2,5,9,7]))


# Q: Problem: Frequency of number
## 1
# def frequency(nums):
#     for val in nums:
#         count = 0
#         for v in nums:
#             if v == val:
#               count += 1
#         print(val, count)

# frequency([1,2,2,3,3,3])

## 2
# def frequency(nums):
#     check = []
#     for val in nums:
#       if val not in check:
#           count = 0
#           for v in nums:
#               if v == val:
#                  count += 1
#           print(val, count)
#           check.append(val)
# frequency([1,2,2,3,3,3])


## Q: Problem: check if two arrays are equal
# ## 1
# def equal(r, p):
#     if len(r) != len(p):
#         return False
#     d = 0
#     while d < len(r):
#       if r[d] != p[d]:
#           return False
#       d += 1
#     return True

# print(equal([2,3,5,4], [2,3,5,4]))

# ## 2
# def equal(r, p):
#     if len(r) != len(p):
#       return False
#     for d in range(len(r)):
#       if r[d] != p[d]:
#         return False
#     return True

# print(equal([2,3,5,4], [2,3,5,4]))


## Q: Problem: first repeating element
# ## 1
# def repeat(nums):
#     val = None
#     for r in range(len(nums)):
#       for p in range(r+1, len(nums)):
#          if nums[r] == nums[p]:
#             val = nums[r]
#     return val

# print(repeat([4,5,1,2,3,5,1]))

# ## 2
# def repeat(nums):
#   for r in range(len(nums)):
#      for p in range(r+1, len(nums)):
#        if nums[r] == nums[p]:
#          return nums[r]

# print(repeat([4,5,1,2,3,5,1]))


## Q: Problem: find common elements between two arrays
# ## 1
# def common(r, p):
#     check = []
#     for d in range(len(r)):
#       for c in range(len(p)):
#         if r[d] == p[c]:
#           check.append(r[d])
#     return check

# print(common([5,2,6,3,4], [3,4,5,6,9]))

# ## 2
# def common(r, p):
#     check = []
#     for d in r:
#       if d in p:
#         check.append(d)
#     return check

# print(common([5,2,6,3,4], [3,4,5,6,9]))


## Q: largest difference in an array
## 1
# def difference(num):
#     big_diff = 0
#     for n in range(len(num)-1):
#        d = num[n+1] - num[n]
#        if d > big_diff:
#          big_diff = d
#     return big_diff

# print(difference([3,7,2,9,4]))

# ## 2
# def difference(num):
#     big_diff = 0
#     for r in range(len(num)):
#       for p in range(len(num)):
#         d = num[r] - num[p]
#         if d < 0:
#           d = -d
#         if d > big_diff:
#             big_diff = d
#     return big_diff

# print(difference([3,7,2,9,4]))






        
            
            





    
        
    