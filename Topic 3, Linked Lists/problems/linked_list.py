# Q: Problem: Insert Node Between Increasing Order Break
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def order(head, val):
#   new = Node(val)
#   curr = head
#   while curr.next:
#     curr = curr.next
#   curr.next = new
#   return head

# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(10)
# head.next.next.next = Node(14)
# res = order(head, 8)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def order(head, val):
#   new = Node(val)
#   if val < head.data:
#     new.next = head
#     return new
#   curr = head
#   while curr.next and curr.next.data < val:
#     curr = curr.next
#   new.next = curr.next
#   curr.next = new
#   return head

# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(10)
# head.next.next.next = Node(15)
# res = order(head, 9)

# while res:
#   print(res.data)
#   res = res.next
  
  
## Q: Problem: Remove Nodes Smaller Than Next Node 
##1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head):
#   curr = head
#   while curr and curr.next:
#     if curr.data < head.data:
#       curr = curr.next
#     else:
#       break
#   return curr

# head = Node(6)
# head.next = Node(5)
# head.next.next = Node(10)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(8)
# res = remove(head)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None
    
# def remove(head):
#   curr = head
#   prev = None

#   while curr and curr.next:
#     if curr.data < curr.next.data:
#       if prev:
#         prev.next = curr.next
#       else:
#         head = curr.next
#       curr = curr.next
#     else:
#       prev = curr
#       curr = curr.next
#   return head

# head = Node(5)
# head.next = Node(3)
# head.next.next = Node(10)
# head.next.next.next = Node(2)
# head.next.next.next.next = Node(8)

# res = remove(head)
# while res:
#   print(res.data)
#   res = res.next

## 3
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head):
#   prev = None
#   curr = head
#   while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
#   head = prev  

#   max = head.data
#   curr = head
#   while curr and curr.next:
#     if curr.next.data < max:
#       curr.next = curr.next.next
#     else:
#       curr = curr.next
#       max = curr.data

#   prev = None
#   curr = head
#   while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
#   return prev

# head = Node(5)
# head.next = Node(3)
# head.next.next = Node(10)
# head.next.next.next = Node(2)
# head.next.next.next.next = Node(8)

# res = remove(head)
# while res:
#     print(res.data)
#     res = res.next


## Q: Problem: Swap the first and last Nodes 
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def swap(head):
#   first = head
#   curr = head
#   while curr.next:
#     curr = curr.next
#   last = curr
  
#   first.data, last.data = last.data, first.data
#   return head

# head = Node(6)
# head.next = Node(7)
# head.next.next = Node(8)
# head.next.next.next = Node(9)
# head.next.next.next.next = Node(10)
# res = swap(head)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#    self.data = data
#    self.next = None

# def swap(head):
#   prev = None
#   curr = head
  
#   while curr.next:
#     prev = curr
#     curr = curr.next
    
#   last = curr
#   prev.next = head
#   last.next = head.next
#   head.next = None
#   head = last
#   return head

# head = Node(6)
# head.next = Node(7)
# head.next.next = Node(8)
# head.next.next.next = Node(9)
# head.next.next.next.next = Node(10)
# res = swap(head)

# while res:
#   print(res.data)
#   res = res.next


## Q: Problem: Detect and remove cycle in a Linked List
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next
    
# def cycle(head):
#   if head.next == head:
#     head.next == None
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next

## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next
    
# def cycle(head):
#   if head.next == head:
#     head.next = None
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)
# head.next.next.next.next.next = head.next.next

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next

## 3
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next

# def cycle(head):
#   slow = head
#   fast = head
  
#   # detect cycle
#   while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#       break
#   else:
#     return head
  
#   slow = head
#   while slow != fast:
#     slow = slow.next
#     fast = fast.next
    
#   ptr = fast
#   while ptr.next != fast:
#     ptr = ptr.next
#   ptr.next = None
  
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)
# head.next.next.next.next.next = head.next.next

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next


## Q: Problem: Merge the two Sorted Lists
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def merge(r, p):
#   curr = r
#   while curr.next:
#     curr = curr.next
#   curr.next = p
#   return r

# r = Node(1)
# r.next = Node(5)
# r.next.next = Node(9)

# p = Node(3)
# p.next = Node(7)
# p.next.next = Node(11)

# res = merge(r, p)
# while res:
#   print(res.data)
#   res = res.next

## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def merge(r, p):
#   fake = Node(-1)
#   tail = fake
#   while r and p:
#     if r.data < p.data:
#       tail.next = r
#       r = r.next
#     else:
#       tail.next = p
#       p = p.next
#     tail = tail.next
  
#   if r:
#     tail.next = r
#   if p:
#     tail.next = p
#   return fake.next

# r = Node(1)
# r.next = Node(5)
# r.next.next = Node(9)

# p = Node(3)
# p.next = Node(7)
# p.next.next = Node(11)

# res = merge(r, p)
# while res:
#   print(res.data)
#   res = res.next


## Q: Problem: Count number of nodes in a linked list:
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def num_count(head):
#   count = 0
#   curr = head
#   while curr:
#     if curr == head:
#       count += 1
#     count = curr.next 
#   return count

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# res = num_count(head)
# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def num_count(head):
#   count = 0
#   curr = head
  
#   while curr:
#     count += 1
#     curr = curr.next
#   return count

# head = Node(5)
# head.next = Node(6)
# head.next.next = Node(7)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(9)

# res = num_count(head)
# print(res)


## Q: Problem: Reverse Linked List in Pairs
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def reverse(head):
#     curr = head
#     prev = curr
    
#     while prev and curr.next:
#       test = curr.data
#       curr.data = curr.next.data
#       curr.next.data = test
#       curr = curr.next.next
#     return head

# head = Node(2)
# head.next = Node(3)
# head.next.next = Node(4)
# head.next.next.next = Node(6)
# head.next.next.next.next = Node(7)

# res = reverse(head)
# while res:
#   print(res.data)
#   res = res.next

## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def reverse(head):
#   fake = Node(0)
#   fake.next = head
#   prev = fake
  
#   while fake.next and prev.next:
#     first = fake.next
#     second = first.prev.next
#     first.next = second.next
#     prev.next = first
#     prev.next = second
#     prev = first
    
#   return fake.next

# head = Node(2)
# head.next = Node(3)
# head.next.next = Node(4)
# head.next.next.next = Node(6)
# head.next.next.next.next = Node(7)

# res = reverse(head)
# while res:
#   print(res.data)
#   res = res.next
  
## 3
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def reverse(head):
#   fake = Node(0)
#   fake.next = head
#   prev = fake
  
#   while prev.next and prev.next.next:
#     first = prev.next
#     second = first.next
#     first.next = second.next
#     second.next = first
#     prev.next = second
    
#     prev = first
#   return fake.next

# head = Node(2)
# head.next = Node(3)
# head.next.next = Node(4)
# head.next.next.next = Node(5)
# head.next.next.next.next = Node(6)

# res = reverse(head)
# while res:
#  print(res.data)
#  res = res.next


## Q: Problem: Remove Nth Node From End
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head):
#   count = 0
#   curr = head
#   while curr:
#     curr = curr.next
#     count += 1
    
#   curr = head
#   for i in range(curr - 1):
#     curr[i] = curr.next
#   return head

# head = Node(5)
# head.next = Node(6)
# head.next.next = Node(7)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(9)
# head.next.next.next.next.next = Node(10)
# res = remove(head, 3)

# while res:
#  print(res.data)
#  res = res.next

## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head, n):
#   count = 0
#   curr = head
#   while curr:
#     count += 1
#     curr = curr.next
  
#   pos = count - n
#   curr = head
#   for i in range(pos - 1):
#     curr[i] = curr.next
  
#   curr.next = curr.next.next
#   return head

# head = Node(5)
# head.next = Node(6)
# head.next.next = Node(7)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(9)
# head.next.next.next.next.next = Node(10)
# res = remove(head, 3)

# while res:
#  print(res.data)
#  res = res.next

## 3
# class Node:
#   def __init__(self, data):
#    self.data = data
#    self.next = None

# def remove(head, n):
#   fake = Node(0)
#   fake.next = head
  
#   fast = fake
#   slow = fake
#   for _ in range(n):
#     fast = fast.next
  
#   while fast.next:
#     fast = fast.next
#     slow = slow.next
#   slow.next = slow.next.next
#   return fake.next

# head = Node(5)
# head.next = Node(6)
# head.next.next = Node(7)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(9)
# head.next.next.next.next.next = Node(10)
# res = remove(head, 3)

# while res:
#  print(res.data)
#  res = res.next


 ## Q: Problem: Check if Linked List is Palindrome
 ## 1
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def palindrome(head):
  list = []
  curr = head
  while curr:
    curr = curr.next
    list.append(curr.data)
  
  left = 0
  right = len(list)
  
  while left < right:
    if list[left] != list[right]:
      return False
  return True

head = Node(1)
head.next = Node(4)
head.next.next = Node(1)
head.next.next.next = Node(1)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(1)

print(palindrome(head))
  
    
  
     
  
  

 

 