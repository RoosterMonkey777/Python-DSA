# - Python Lists are ordered collections of data just like arrays (in other programming languages)
# - Allows for different types of elements to be in the list
# - Similar to Vectors in C++ and ArrayList in Java
# - Costly operation is 'inserting' or 'deleting', from the beginning of the list, as all subsequent elements need to be shifted 

# ------------------------------------------------------------------------------------------------------------
List = [1,2,3,"GFG", 2.3]
print(List)

# - Lists are simples containers and need not be homogeneous
# - Lists are mutable (they can be altered after creation)

# Python Program to demonstrate 

List = []
print("Blank List:" )
print(List)

# Creating list of numbers
List = [1,2,3,4,5]
print('\nList of numbers: ')
print(List)

# Creating list of strings and accessing using index
List = ["Hello", "Cheese", "Goat"]
print('\nList Items: ')
print(List[0])
print(List[2])

## Complexities of Creating Lists
# - Time Complexity: O(1)
# - Space Complexity: O(n)
# ------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------
## Example 2: Creating List with multiple distinct or duplicate elements
# - A list may contain duplicate values with their distinct positions
# - Multiple distinct or duplicate values can be passed as sequence at time of list creation

# Creating a List with use of Numbers (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
 
# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)
# ------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------
## Accessing Elements from the List:

# Python program to demonstrate accessing of element from list
 
# Creating a List with the use of multiple values
List = ["Geeks", "For", "Geeks"]
 
# accessing a element from the list using index number
print("\nAccessing a element from the list")
print(List[0])
print(List[2])
# ------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------
## Accessing elements from a multi-dimensional list:
# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
 
# accessing an element from the Multi-Dimensional List using index number
print("\nAccessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
# ------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------
## Negative Indexing:
# - Negative sequence indexing represent postions from the end of list
# - Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]
# - Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

List = [1, 2, 'Geeks', 4, 'Red', 6, 'Zookeeper']

# accessing an element using negative indexing
print("\nAccessing element using negative indexing")

# print the last element of list
print(List[-1])
# print the third last element of list
print(List[-3])
# ------------------------------------------------------------------------------------------------------------