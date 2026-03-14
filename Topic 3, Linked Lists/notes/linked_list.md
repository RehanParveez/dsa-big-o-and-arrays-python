## Linked Lists

# What is Linked List?
A linked list is a type of linear data structure in which the elements ate stored in the form of nodes, and here the key concept is each node present points to the next node, so this is how the basic flow in the linked lists properly work.

- one more point here compared to arrays in linked lists the opposite happens, like in linked lists elements are not stored next to each other in the memory, this does not happen, rather each elements which are present next to each other they store the refernce to the next element.

- for example:
[10 | next] then -> [25 | next] then -> [45 | next] and then -> [65 | None]

. now here as different blocks are present, these all individual blocks are called Node, and the each nodes contains some value of data and also a pointer called next which has the address of the next element present.

# Importance of Linked Lists:
Now the point here is the importance of linked lists is quite much bcz there is a problem with the use of data structures like arrays, the problem is these store elements in a contiguous memory form which means when the object or values are present close to each other like almost at a touching distance to each other.

for example in this array pf numbers:
[10, 20, 30, 40]

now here the memory layout simply looks like,
90 -> 10
94 -> 20
98 -> 30
102 -> 40

also this way of being present shows these exist in the continuous form.

. Now being present in such form at one side gives the advantages like:

- Fast indexing -> O(1) means by simply calling the:

arr[2]
the index can be aaccessed quite quickly, but here this way also causes the problems like:

# Problem 1: Insertion:
Now here if the task is to insert the value of number in the center of this numbers array:

the array is -> [10, 20, 30, 40] and the task here is to:
- insert the number 11 at the index 1

now in order to do this first thing here is changing the position of numbers like:
[10, 11, 20, 30, 40]

so this is exactly the problem with this approach which causes the problem of time complexity like the numbers which are present after the target number there position gets changed bcz of just one insertion of a number in between them:

O(n)

# Problem 2: Deletion:
Deleting an element, now for example if the task is to delete an specific element from the array of numbers then again that requires a change in the position of all the other numbers.

for example deleting an number 10 which is present at the index 0 now this again will cause the change in the positions of all other numbers like:

the array is -> [10, 11, 20, 30, 40] and the task here is to:
- delete the number 10 present at the index 0

Now this problem of time complexity caused by the use of array is what the use of linked lists solve and this happens like instead of changing the position of the elements, simply the use of change of pointers can be done.

for example:
present:
10 -> 20 -> 30

now the task is -> insert number 15 after the number 10:
10 -> 15 -> 20 -> 30

so in this case only the change of pointer happens.

# Node Structure:
The topic of node structure is related to understanding like how every linked list is made by using the nodes.

Further the each node has two main things inside it:
1. data
2. pointer -> which acts like a reference 

now in order to implement this node concept working it is done with the use of a class like:
for example:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

now here in this class:
. the self.data part -> stores the value,
. and the self.next part -> stores the reference to the next node present alongside it.

# Display of Memory:
now in order to understand how the memory is displayed in node structures then lets take this example:
5 -> 10 -> 15

now according to this the memory will look like this:

In node A -> the address is 50
data = 5
next = 52

In node B -> the address is 52
data = 20
next = 54

In node C -> the address is 54
data = 30
next = None

- now important point to consider here is the nodes can be present anywhere inside the memory so bcz of this it is called as linked structure.

# Head Pointer:
One more important concept in linked lists is like these always start with a head pointer,

for example:
head -> 10 -> 20 -> 30 -> None
. Now according to this example the head is the one which stores the address of the first node.
. So this means if a head is not present than the -> list is simply lost.


## Types of Linked Lists:
Now there are two main types of linked lists which are:

1. Singly linked Lists
2. Doubly Linked List

# Singly Linked List
a singly linked List is the type of linked lists in which the each node has two main things:

. data, and the
. next pointer

the structure of a simple singly linked list is as given:

5 -> 10 -> 15 -> 20 -> None
this is similar to the structure of basic linked list which was used above.

# Traversal direction:
the singly linked lists are those which have the traversal direction of only moving forward.

-- code example:

- Class of Node:
class Node:
   def __init__(self, data):
   self.data = data
   self.next = None

- Class of LinkedList 
class LinkedList:
  def __init__(self):
    self.head = None

# Meaning of traversal:
The concept of traversal in linked lists means visiting the position of every node present in the class.

for example:
7 -> 14 -> 21 -> None
now here traversal would mean starting from first node for instance and then keep moving until the pointer of None which is present.

-- code example:
def list(self):
  prac = self.head
  while prac:
    print(prac.data)
    prac = prac.next

now in this method the variable prac is equal to -> head, and this prac variable will keep moving in the list until the value of prac variable becomes equal to the value of None.

. And here if time complexity is measured then it would be:
O(n) 
and the big O(n) means the execution of complexity related to the time and space move/increases related with the increase of the input size.

# Operations of Insertion in Singly Linked List:
Some of the important operations related to insertion are:
. inserting at the beginning,
. inserting at the end,
. inserting in the middle,
. inserting at the Beginning

for example:
first:
5 -> 10 -> 20
and after inserting number 15, then it becomes:
5 -> 10 -> 15 -> 20

and this simple inserting work happens as:
1. creating a new node,
2. then after this that new.next is used to point to the head,
3. and this is how the update of the head is completed

- code example:
def insert(self, data):
  new = Node(data)
  new.next = self.head
  self.head = new

and according to this example the time complexity is O(1) which simply means the time consumption is going to be constant regardless the increase of the input size.

- Inserting at the end:
for example:
5 -> 10 -> 15
then after inserting number 20 at the end:
5 -> 10 -> 15 -> 20

- code example:
def end(self, data):
  new = Node(data)
    if self.head is None:
      self.head = new
      return

    current = self.head
    while current.next:
      current = current.next
    current.next = new

now the time complexity for this example is O(n) which means the time consumption is going to be increased as the size of the input increases.

- Inserting after a node:
for example:
5 -> 10 -> 20
now inserting the number 15 after the number 10.
5 -> 10 -> 15 -> 20

- how this is happening by logic?
new.next = current.next
current.next = new

# Deletion Operation:
deleting a node, now for this the example is:
5 -> 10 -> 15 -> 20
now deleting the number 15 so it becomes like:
5 -> 10 -> 20

- how this is done?

1. first finding of the previous node is done,
2. then the changing of the pointer is done, and then this happens,
10.next = 20

code example:
def delete(self, check):
  current = self.head
  previous = None

    while current:
      if current.data == check:
        if previous:
          previous.next = current.next
        else:
          self.head = current.next
        return

        previous = current
        current = current.next

Key Note here is:
In linked lists thefast indexing is compromised so that the fast insertion can be done.


## Doubly Linked List:
now the second type of linked lists which is doubly linked list, now in it the each node has three components:
. data
. next pointer
. previous pointer

the structure for this would look like:
None <- 10 -> 20 -> 30 -> None
           <-    <-

- advantages of doubly linked list:

. It helps to traverse in the forward and backward direction,
. It also helps in the process of easier deletion 

- Reference of the node structure:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

- now in this above given example structure is like:
Node1
data = 5
next -> Node2
prev -> None

# Insertion Operations in Doubly Linked List:
- Inserting at the beginning:
new.next = head
head.prev = new
head = new

# The Concept of Fast and Slow Pointer Pattern:
Now this is one of the most important concept in linked lists and commonly it is also called as (Tortoise and the Hare algorithm).
This algorithm was invented by the Robert W. Floyd and his main idea was about -> Use of two pointers:

. slow -> moves 1 step
. fast -> moves 2 steps

- example for the cycle detection of this process is:
1 -> 2 -> 3 -> 4 -> 5
          |     |
          <- <- <-

now using this approach the list forms a loop and compared to this in the normal approach of traversal was used then the list would have been infinite, so this is the key significance of this approach.

- The algorithm example for this approach will look like:
slow = head
fast = head
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next

    if slow == fast:
      cycle exists

now according to this example algorithm structure If there exists a cycle, then the fast pointer will lap the slow pointer, here meaning of lapping means bcz one pointer is fast and the other is slow then within in hte same running cycle, the fast would complete its work and then again it will catch up the slow pointer from behind. so this approach is very useful and efficient.

- code example:

def cycle(head):
  slow = head
  fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

        if slow == fast:
          return True
    return False

. now for this example operation the time complexity -> O(n), which is inc. in time consumption with the inc. in the input size.
. and the space complexity for this operation is -> O(1), which is the time consumption of the operation doesnt depend on the input size.

