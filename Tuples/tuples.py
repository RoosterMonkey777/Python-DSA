## Tuples

# - Python tuples are similar to lists, but they are immutable (cannot be changed after creation)
# - Tuple can also contain elements of various types
# - In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without 
#   the use of parentheses for grouping of the data sequence. 
# Note: To create a tuple of one element there must be a trailing comma. For example, (8,) 
# will create a tuple containing 8 as the element.


#--------------------------------------------------------------------------------------------------------
# Creating a Tuple with the use of Strings
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
     
# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)
print(type(tuple(list1)))
 
# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])
 
# Accessing element from last negative indexing
print("\nLast element of tuple")
print(Tuple[-1])
 
print("\nThird last element of tuple")
print(Tuple[-3])

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
 
# Creating a Tuple with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
 
# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 
# Creating a Tuple with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

Tuple2 = (1,2,3,4,5)
print(Tuple2)
#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------
# Example 2: Creating a Tuple with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)
 
# Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
 
# Creating a Tuple with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)
 
# Creating a Tuple with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

# Complexities for creating tuples:
# Time complexity: O(1)
# Auxiliary Space : O(n)  
#--------------------------------------------------------------------------------------------------------

  
    
#--------------------------------------------------------------------------------------------------------
## Accessing of Tuples
# - Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed 
#   via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their 
#   elements are usually homogeneous and are accessed by iterating over the list.
# Note: In unpacking of tuple number of variables on the left-hand side should equal to a number of values in given tuple a. 


# Accessing Tuple with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])
 
 
# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
 
# This line unpack values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Complexities for accessing elements in tuples:
# Time complexity: O(1)
# Space complexity: O(1)
#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------
## Concatenation of Tuples
# - Concatenation of tuple is the process of joining two or more Tuples. 
# - Concatenation is done by the use of ‘+’ operator. 
# - Concatenation of tuples is done always from the end of the original tuple. 
# - Other arithmetic operations do not apply on Tuples. 
# Note- Only the same datatypes can be combined with concatenation, error arises if a list and a tuple are combined.

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
 
Tuple3 = Tuple1 + Tuple2
 
# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)
 
# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)
 
# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)

# Time Complexity: O(1)
# Auxiliary Space: O(1)
#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------
## Slicing of Tuple
# - Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. 
# - Slicing can also be done to lists and arrays. 
# - Indexing in a list results to fetching a single element whereas Slicing allows to fetch a set of elements. 
# Note- Negative Increment values can also be used to reverse the sequence of Tuples.


# Slicing of a Tuple with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')
 
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])
 
# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])
 
# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

# Complexities for traversal/searching elements in tuples:
# Time complexity: O(1)
# Space complexity: O(1)
#--------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------
## Deleting a Tuple
# - Tuples are immutable and hence they do not allow deletion of a part of it. 
# - The entire tuple gets deleted by the use of del() method. 
# Note- Printing of Tuple after deletion results in an Error. 

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1
 
# print(Tuple1) # results in error
#--------------------------------------------------------------------------------------------------------


# Tuples vs Lists:

# Similarities:
# - Function that can be used for both tuples and lists:
#   len(), max(), min(), sum(), any(), all(), sorted()
# - Methods that can be used for both lists and tuples:
#   count(), index()
# - Tuples can be stored in lists
# - Lists can be stored in tuples
# - Both can be nested

# Differences:
# - Methods that cannot be used for tuples:
#   append(), insert(), remove(), pop(), clear(), sort(), reverse()
# - generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
# - Iterating through a ‘tuple’ is faster than in a ‘list’.
# - ‘Lists’ are mutable whereas ‘tuples’ are immutable.
# - Tuples that contain immutable elements can be used as a key for a dictionary.