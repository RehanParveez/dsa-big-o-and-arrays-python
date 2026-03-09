## Hashing Concept:

# What is Hashing?

Hashing is a method in which we take some data like for example a number, string, or an object and then we do the conversion of it into a value of fixed size which is called a 'hash' and this is done by using the function of hash. Next this hash then acts like an a index or a key which then tells the given program like where to store or get the data properly.

-- An example for this would be:
like imagine a library which has hundreds and thousands of books, now here instead of searching randomly like rack by rack, what we can do best is using hashing according to which in this context of library for example every book has a unique catalog number which is called hash.

so by using this we will go directly to that exact rack by using that specific number and by this way searching or excessing of that book for instance would be quite fast and efficient.

- Why Hashing is Useful?
. so as we talked above by using the hashing the processes like search, insertion, and deletion these become fast.
. it helps in counting efficiently like for instance how many times a specific element is present in a data set.
. it will help in detecting duplicates quickly.
. the use of hashing reduces the operations from O(n²) complexity which is also called brute force it reduces this to O(n) in majority of the cases, which again makes it special.


# Use of Hashing in Python:
when we talk about hashing in python it gives some built in data structures which are based on hash:

# 1. Dictionaries also called as dict:
now this data structure of python stores the data in key value pairs and also in it the keys are hashed automatically like for example:

# A: dictionary to count animals:
animal_count = {}
animal_count['jiraffe'] = 3
animal_count['wolf'] = 2

print(animal_count['jiraffe'])  -> now here the result is O(1) and the access of value is -> 3

- Key point:
 all the operations like lookup, insert, and delete all these are of O(1) complexity on average, and this is mainly bcz python simply calculates the hash of the key and then it jumps to the location directly.

# B: Sets also called as set:
in python the sets are used as a data structure which only stores the unique elements.

. firtly here python will hash the each and every element automatically.

- For Example:
num = set()
num.add(5)
num.add(7)
num.add(5)  -> now here bcz this num 5 is repeating so its a duplicate therefore it will be ignored, now when we gonna print the num then the output we gonna get is 5, 7.
print(num)  -> {5, 7}

- further if we do print(7 in num) -> then its going to be of complexity O(1) and here the lookup is going to be of boolean value-> True

-- Key point:
if we talk about sets then they are great for the checks of membership and also for removing the duplicate values.

# C: How Python internally handles the hashing?
hash table of python = boxes for storage (an array) + hash function.

-- Now key steps while adding a key:
. Compute the hash(key) and it is done in the form of -> integer,
. Then converting the hash(key) in to a index,
. Further then storing the value in the specific boxes for the storage at that particular index.


# Hashing vs Arrays: The Big-O Comparison:

# Operation	        Array	           Hash Table(dict/set)
Insert	            O(1)(at end)	   O(1) average
Lookup/Search	    O(n)	           O(1) average
Delete	            O(n)	           O(1) average
Counting/Tracking	O(n²)              O(n) using hash

. Now important thing is as i studied earlier like arrays require the linear search in order to find an element.
. but the concept of hashing is the one which allows the direct access as it offers fast search like operations, so it as i studied can be considered as an (smart array) which has its individual components calculated properly.

# -- Use of hashing in some key previously solved problems:

# 1: Q Problem: Count how many times each element occurs:
arr = [1, 2, 2, 3, 3, 3]
count = {}

for num in arr:
    if num in count: 
        count[num] += 1
    else:
        count[num] = 1

print(count) 

# now in this problem the output is gonna be this -> {1: 1, 2: 2, 3: 3}
-- Working of the problem.

. firstly here a empty dictionary is declared/initialized which here gonna ->act like a hash table,
. next here we iterate over an array by going to the -> each element and we check if the related key exists or not,
. and then if true then we just update the count or simply initialize it to 1,
. further the lookup count[num] is of O(1) complexity so according to this the full  of numbers is equal to -> O(n),
. lastly here if the hashing was not used then we would have needed to loop over the complete array in order to search the each element, for whihc complexity would have been -> O(n²).


# 2: Q Problem: check if array has duplicates.

nums = [1, 2, 3, 4, 5, 3]
known = set()  # hash table for membership

for num in nums:
    if num in known:
        print('the duplicate is found:', num)
        break
    known.add(num)

now here according to this problem:
. num in known is of complexity ->  O(1)
. if we use the arrays mainly then its gonna be of complexity -> O(n²)
. next if we use hashing then its gonna be of complexity -> O(n)


# 3: Q Problem: find the two numbers that add up to a target.
nums = [2, 7, 11, 15]
target = 9
known = set()

for num in nums:
    res = target - num
    if res in known: 
      print('the pair is found:', (res, num))
        break
    known.add(num)

- now here according to this problem:

. first we iterate over the full array of nums,
. then here the calculation of the res occurs which is as (target - num),
. this particular logic is about checking like if a res really exists in hash table with the complexity of -> O(1),
. and lastly here current calculated number is added to the hash table for further checking/searching.

# The concept of time complexity in hashing: O(n)
the point to learn here is if we dont use hashing concept then the use of -> nested loops is required which has the complexity of -> O(n²)

# 4: Q Problem: the first non repeating element:

alpha = ['a', 'b', 'c', 'a', 'b', 'd']
count = {}
for ch in alpha:
    count[ch] = count.get(ch, 0) + 1 

for ch in alpha:
    if count[ch] == 1:
        print('first nonrepeating ch is:', ch)
        break

in the above problem the key part of hte logic is:

. first we count all the alphabets/elements in an array, and all of this has the complexity of -> O(n),
. then we traverse/check the full array of elements to find the first unique one of them, and here the complexity is -> O(n),
. so thats how in situation like these the use of hashing concept gives the fast results like fast counting and then the access of values.


# Practical hashing understanding:
the hashing concept can be seen as:
. Hash Table = array of boxes  -> now here the different addresses can be saved
. Keys = unique labels -> the value stored in keys is needed ot be unique and calling it labels means it present here as a label and when calling on that label which is unique then the specific value related to that is obtained,
. so the hash function in this situation is the one which simply -> calculates like in which particular box the key should be placed.
. And as the key is there so on calling that key the value is generated which was -> stored inside that box we talked about like array of boxes.

- For Example:

# Key (num)     Hash Index	   Value
12	            2	           12
22	            3	           22
32	            2	           32 (collision handled internally)


## Collision concept in Hashing:

