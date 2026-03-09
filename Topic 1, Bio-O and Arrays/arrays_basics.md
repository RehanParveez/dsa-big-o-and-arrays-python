## Concept of Arrays:

# What is array?
The array in simple terms can be explained as the:
collection of the elements which are stored alongside the memory locations of each others.

Now related to this while using the python language we use one of the data structures which is lists, for example:

nums = [10, 20, 30]
and here this number variable can be considered as an array.

# Why the arrays are important?
here one of the key concept is of indexing,
 now as in the:
num[0] -> this is referring to the exact index on which the num 0 is present, similarly:
num[1] -> this is referring to the exact index on which the num 1 is present.

and this exact index concept is what we studied in the learning of O(1), and so now the example of two numbers given with their index is also referring to the concept of O(1), and also one more key thing is,
. The python calculates the location of the memory directly.

## Some common operations of arrays and their complexity:
# Operation	         Complexity
Access by index	       O(1)
Update value	       O(1)
Traverse	           O(n)
Search (unsorted)	   O(n)
Insert at end	       O(1) average
Insert at beginning	   O(n)

-- here if we talk about now the insert at beginning then why its complexity is O(n)? then the reason is because we gonna insert the new number at the beginning so then all the other numbers will move also bcz of this.

Now lets understand each of the operations alongside their complexity one by one. 

1. Access by index — O(1):
it simply means the accessing of the given number using its index, so it will take the constant time each and every time, like no matter how big the array is,

-- The main logic behind it:
The thing is the arrays store the given elements like for example numbers in the continuous memory, so thats why the given system say computer it will directly calculate the address by using the formula:

address = base_address + (index × element_size)

2. Update value — O(1):
this operation of the big O complexity simply means while we change a value at a given specific index then it always takes a constant time, and this happens because see once we know the location of a index particularly so then the value is easily replaced in that slot of memory.

- for example:

num[2] = 50
so here we know the index and the what value is present at it, so here no searching is needed.


3. Traverse — O(n):
now this operation of the big O complexity simply means as the name suggests traversing which means visiting the every element let suppose every number in the array.

- for example:

for i in arr:
    print(i)

so this loop shows like if the array has n numbers in it for instance, so then the loop will run that n times.

4. Search (unsorted) — O(n):

now next this operation of the big O complexity simply means as the name suggests searching, lets suppose for a specific value in an unsorted array, so this will require the checking of the each element one by one.

for example:
for i in arr:
   if i == target:
      return True

so here in this simple loop with a if condition, now in this lets suppose a worst case scenario like the element to be found is present at the last position, so then we need to check all the n elements, which is not that good also.

5. Insert at end — O(1) average:

now next this operation of the big O complexity simply means as the name suggests adding, so in this case if we are to add an element at the end then usually it will take the same constant time.

- for example:

arr.append(10)

so in this case trying to append a value in the arr and by default it will we appendid at the end, now point is like usually the array has an extra given memory, so thats why here the element is going to be simply appendid at the end of an array.

important point:
while studying it was given that sometimes the arrays size should be changed so in that particular case it will take O(n) complexity, but the point is that rarely happens so the average times the result of the big o O(1) occurs.

6. Insert at beginning — O(n)

now next this operation of the big O complexity simply means again as the name suggests inserting, so lets suppose inserting the value at the start, so like this will require the repositioning of all the existing elements.

- for example:

[10, 20, 30]
so now if we want to Insert a new value say 5 at start, then this list would become -> [5, 10, 20, 30]

now this shows like to add a new value at start, then every present element should move a one value to the right, and for this to happen it will require the n times of operations.

## Some important array techniques

these few techniques are very important like:

# Two Pointers:
this technique is used like when:

. we are working from both the ends,
. we are comparing the pairs,
. and then when we are reversing, means totally rearranging the given values.

for example:
left = 0
right = len(arr) - 1
while left < right:
    left += 1
    right -= 1

# Sliding Window
and this technique is used when we are working with the subarrays like:

. The continuous segments
. Finding the minimum/maximum sum value

# Prefix Sum

and next this technique is used when we need to perform actions like:

. Precomputing the cumulative sum
. Optimizing the nested loops
