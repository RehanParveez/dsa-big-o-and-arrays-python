## Q: Problem: The Check of Valid Parentheses:
## 1
# def valid(val):
#   c1 = 0
#   c2 = 0
#   for v in val:
#     if v == '(':
#       c1 = c1 + 1
#     if v == ')':
#       c2 = c2 + 1
#   if c1 == c2:
#     return True
#   else:
#     return False

# print(valid('('))  
# print(valid('()')) 
# print(valid(')(')) 

## 2
# def valid(val):
#   check = []
#   for v in val:
#     if v == '(':
#       check.append(v)
#     if v == ')':
#       if len(check) > 0:
#         check.pop()
#       else:
#         return False

#   if len(check) == 0:
#     return True
#   else:
#     return False

# print(valid('('))  
# print(valid('()')) 
# print(valid(')(')) 

## 3
# def valid(val):
#   check = []
  
#   for v in val:
#     if v == '(':
#       check.append(v)
#     elif v == '[':
#       check.append(v)
#     elif v == '{':
#       check.append(v)
    
#     elif v == ')':
#       if len(check) == 0:
#         return False
#       first = check[-1]
#       if first == '(':
#         check.pop()
#       else:
#         return False
    
#     elif v == ']':
#       if len(check) == 0:
#         return False
      
#       first = check[-1]
#       if first == '[':
#         check.pop()
#       else:
#         return False
    
#     elif v == '}':
#       if len(check) == 0:
#         return False
#       first = check[-1]
#       if first == '{':
#         check.pop()
#       else:
#         return False
    
#   if len(check) == 0:
#     return True
#   else:
#     return False 

# print(valid('(]'))  
# print(valid('()')) 
# print(valid(')(')) 
# print(valid('()[]{}')) 
# print(valid('([{}])')) 


## Q: Problem: Reverse a String
## 1
# def reverse(str):
#   return str[::-1]

# print(reverse('reverse')) 
# print(reverse('traverse'))

## 2
# def reverse(str):
#   check = []
  
#   for s in str:
#     check.append(s)
#   store = ''
#   for val in range(len(check)):
#     store = check[val]
#   return store

# print(reverse('reverse')) 
# print(reverse('traverse'))

## 3
# def reverse(str):
#   check = []
  
#   for s in str:
#     check.append(s)
#   store = ''
#   while len(check) > 0:
#     s = check.pop()
#     store = store + s
#   return store

# print(reverse('reverse'))
# print(reverse('traverse'))


## Q: Problem: Find Next Greater Element
## 1
# def greater(num):
#   res = []
#   for n in range(len(num)):
#     for n2 in range(len(num)):
#       if num[n2] > num[n]:
#         num = num[n2]
#     res.append(num)
#   return res

# print(greater([4, 3, 4, 6, 5])) 
# print(greater([6, 5, 4, 3, 2, 1])) 

## 2
# def greater(num):
#   check = []
#   for n in range(len(num)):
#     check.append(num[n])
#   for n in range(len(num)):
#     if len(check) > 0:
#       n2 = check
#       if num[n] < num[n2]:
#         n = num[n2]
#   return check

# print(greater([4, 3, 4, 6, 5])) 
# print(greater([6, 5, 4, 3, 2, 1])) 

## 3
# def greater(num):
#   check = []
#   res = [-1] * len(num)
#   for n in range(len(num)):
#     check.append(num[n])
#   for n in range(len(num)):
#     if len(check) > 0:
#       first = check[-1]
#       if first > num[n]:
#         res[n] = first
#   return res

# print(greater([4, 3, 4, 6, 5])) 
# print(greater([6, 5, 4, 3, 2, 1])) 

## 4
# def greater(num):
#   check = []
#   res = [-1] * len(num)

#   for n in range(len(num)):
#     while len(check) > 0:
#       last = check[-1]
#       if num[n] > num[last]:
#         check.pop()
#         res[last] = num[n]
#       else:
#         break
#     check.append(n)

#   return res

# print(greater([4, 3, 4, 6, 5])) 
# print(greater([6, 5, 4, 3, 2, 1])) 


## Q: Problem: Remove Adjacent Duplicates
## 1
# def remove(d):
#   d = d.replace('nnn', '')
#   d = d.replace('sss', '')
#   return d

# print(remove('annnaca'))
# print(remove('azsszy'))

## 2
# def remove(s):
#   res = ''
#   for ch in s:
#     if ch not in res:
#       res = res + ch
#   return res

# print(remove('annnaca'))
# print(remove('azsszy'))

## 3
# def remove(val):
#   check = []
#   for v in val:
#     if len(check) == 0:
#         check.append(v)
#     else:
#       first = check[-1]
#       if first == v:
#         check.pop()
#       else:
#         check.append(v)
#   res = ''

#   for v in check:
#     res = res + v
#   return res

# print(remove('annnaca'))
# print(remove('azsszy'))


## Q: Problem: Min Stack check
## 1
class MinStack:
  def __init__(self):
    self.check = []
  def push(self, v):
    self.check.append(v)
  def pop(self):
    self.check.pop()
  def Min(self):
    return min(self.check)

obj = MinStack()
obj.push(6)
obj.push(7)
print(obj.Min())   

obj.push(4)
obj.push(3)
print(obj.Min())   

obj.pop()
print(obj.Min())


    








