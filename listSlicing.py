## Slicing of a List

# We can get substrings and sublists using a slice. 
# In Python List, there are multiple ways to print the whole list with all the elements 
# To print a specific range of elements from the list, we use the Slice operation. 

# Slice operation is performed on Lists with the use of a colon(:)

# To print elements from beginning to a range use:
# [: Index]

# To print elements from end-use:
# [:-Index]

# To print elements from a specific Index till the end use 
# [Index:]

# To print the whole list in reverse order, use 
# [::-1]

# Python program to demonstrate slicing of elements in a List
 
# Creating a List
List = ['B', 'U', 'T', 'T', 'H', 'E','A', 'D', 'M', 'E', 'E', 'K', 'S']
print("\nInitial List: ")
print(List)
 
# Print elements of a range using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th element till the end: ")
print(Sliced_List)

# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)


## Negative Index Slicing:

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']
print("\nInitial List: ")
print(List)
 
# Print elements from beginning to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)
 
# Print elements of a range using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)
 
# Printing elements in reverse using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
 
 

