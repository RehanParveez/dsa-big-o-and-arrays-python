## Q: array sorting
# ## 1
# def sorted(num):
#     for val in range(len(num) - 1):
#         if num[val] > num[val + 1]:
#             return False
#     return True

# # print(sorted([1, 3, 4, 6, 7, 8, 9]))
# print(sorted([1, 3, 2, 5, 4, 7, 6, 8, 9]))

## 2
def sortedd(num):
    behind = num[0]
    for val in num:
        if val < behind:
            return False
        behind = val
    return True

# print(sortedd([1, 2, 3, 4, 5]))
print(sortedd([5, 2, 6, 4, 1, 7, 9]))


