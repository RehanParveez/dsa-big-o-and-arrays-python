## Q: Problem: find the most frequent word
## 1
# def frequent(words):
#     count = {}
#     max_count = 0
#     for word in words:
#        if word not in count:
#           count[word] = 1
#        else:
#           count[word] += 1
#        if count[word] > max_count:
#           count = word
#     return count

# print(frequent(['apple','banana','apple','orange','apple','banana']))

## 2
# def frequent(words):
#     count = {}
#     max_word = ""
#     max_count = 0
#     for word in words:
#       if word in count:
#         count[word] += 1
#       else:
#         count[word] = 1
        
#       if count[word] > max_count:
#         max_count = count[word]
#         max_word = word
        
#     return max_word
# print(frequent(['apple','banana','apple','orange','apple','banana']))


## Q: Problem: check if given two strings are Isomorphic

## 1
# def isomorphic(d, a):
#     check = {}
#     for c in range(len(d)):
#         check[d[c]] = a[c]
        
#     for c in range(len(d)):
#         if check[d[c]] != a[c]:
#             return False
#     return True

# print(isomorphic('foo', 'bar'))

## 2
# def isomorphic(d, a):
#     check1 = {}
#     check2 = {}

#     for c in range(len(d)):
#       if d[c] in check1:
#         if check1[d[c]] != a[c]:
#             return False
#       else:
#           check1[d[c]] = a[c]

#       if a[c] in check2:
#         if check2[a[c]] != d[c]:
#            return False
#         else:
#            check2[a[c]] = d[c]
#     return True

# print(isomorphic('paper', 'title'))


## Q: Problem: check if the two arrays contain the same elements
## 1
# def same(num1, num2):
#     return set(num1) == set(num2)

# print(same([1,1,2], [1,2,2]))

## 2
# def same(num1, num2):
#    if len(num1) != len(num2):
#       return False
    
#    count1 = {}
#    for num in num1:
#      count1[num] = count1.get(num, 0) + 1 
#    count2 = {}
#    for num in num2:
#      count2[num] = count2.get(num, 0) + 1
        
#    return count1 == count2

# print(same([1,1,2], [1,2,2]))


## Q: Problem: find the elements that appear in exactly one array
## 1
# def unique(num1, num2):
#   result = []
#   for n in num1:
#      if n not in num2:
#         result.append(n)
#   return result

# print(unique([1,2,3], [2,3,4]))

# ## 2
def unique(num1, num2):
    result = []
    for n in num1:
      if n not in num2:
        result.append(n)
        
    for n in num2:
      if n not in num1:
        result.append(n)
    return result

print(unique([1,2,3], [2,3,4]))


