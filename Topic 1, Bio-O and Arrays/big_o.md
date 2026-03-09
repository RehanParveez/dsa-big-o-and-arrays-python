## Big-O Time Complexity
What it is?
First of all the biog-o natation is a tool used in mathematics especially related to the computer science and it mainly explains the concept of worst case of the time or the space complexity of an algorithm.

-- now here the word algorithm can be defined separately as, the set of instruction is called an algorithm. for example the exact set of instruction/commands in which a program is going to be performed, so this is simply called an algorithm.

# Why do we use the Big-O?

lets consider a a situation here,
. now lets say a solution A takes 1 second in execution for the 100 numbers.
. and the Solution B takes 1 second in execution for the 1000,000 numbers.

-- now which one is better? 
the answer here is clearly B.

The key fact is the Big-O helps us in measuring:

. Like how fast an algorithm is growing as compared to the increasing input size.
. Actually it measures the growth rate.

# Meaning of “n” term?

In the data structure and algorithms(DSA):

n = input size, means what the size of input being given.

Example:

arr = [1,3,5,7,9,11]

now here n = 6,
now even if a array has 1000 elements then -> n in that case would be equal to = 1000

So according to these points the Big-O concept will tell us like:
. If the n becomes very large, then how will the runtime grow?

# Key Types of Big-O 

- O(1) — Constant Time
here big O simple shows that the given runtime does not depend on n.

for example:

def first_numb(arr):
    return arr[0]

so accoridng to this example even if the array has:
. 5 elements
. 1 million elements, we will simply access the index 0 directly.

and so this simply explains -> O(1)

- O(n) — Linear Time
in this concept simply the runtime grows linearly like with the inc. of the input of the size.

for example:
for num in arr:
    print(num)

now here:
. if a -> n = 5 then this simply means -> 5 exact operations,
. and if a -> n = 1000 then this simply means -> 1000 exact operations.

now this simply explains the concept of -> O(n)

- O(n²) — Quadratic Time
in this big O concept this whole process usually happens with the involvement of the nested loops.

for example:
for i in range(n):
    for j in range(n):
        print(i, j)

now acc. to this example:
. If n = 5 then this means -> the involvement of the 25 operations,
. and if n = 1000 then this means -> the involvement of the 1000,000 operations,
. so thats why this type of big O time complexity grows very quickly, 
. and this is the reason also that the O(n²) time complexity is quite dangerous for the big data sets.

- O(log n) — Logarithmic Time:
now this type of big O complexity occurs when the handler let suppose we simply reduce the problem by the half each time.

for example:
Binary search.

. so now If we search in the 1000,000 numbers for instance then,
. we wont check all in a best case scenario and instead of this we will keep dividing it by number 2 -> and doing this would be really good and wise as well.


## Key points to Keep in mind:

-- point 1: Ignoring constants:
for example:

for i in range(n):
    print(i)
for i in range(n):
    print(i)

. now this is simply a 2n operations, bcz it repeats two times, so thats why it is given as 2n,
. but now here at the same time for example in Big-O -> O(n)
. we will simply ignore the constants


-- point 2: Dropping the lower order terms:
to understnad this type of complexity, simply lets suppose,

if the present complexity is:
n² + n
then in this case -> Big-O = O(n²)

the important point to remember here is simply means like when the n becomes quite huge, then the -> n² will dominate the n.


-- point 3: Focusing on the worst case
the key thing to understand hers is see this type of Big-O wll usually describe the very worst case performance which is present.


# The Concept of Time vs Space Complexity:
here in most simple terms:
. The Time = how fast the program/algorithm runs?
. The Space = shows simply lke how much the extra memory it will use or it uses,

for example:

def old_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr

here in this above given example the 'arr' is being passed as the parameter, and we are defining one empty list named as new_arr = [] which will give us the key calculations as:

. The Time complexity as -> O(n), 
. And the Space complexity here is as ->  O(n) -> because mainly the new arr is being created.

