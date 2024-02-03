#------------------------------------------------------------------------------------------------------
## Adding Elements to a Python List

# Method 1: Using append() method
# - Elements can be added to the list by using built-in append() function
# - Only one element at a time can be added to the list by using append() method
# - For the addition of multiple elements with the append() method, loops are used
# - Tuples can also use append method because tuples are immutable
# - Lists can also be added to the existing list with the append() method

# Complexities of Adding elements in a Lists(append() method):
# - Time Complexity: O(1)
# - Space Complexity: O(1)

# Python program to demonstrate addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the list using Iterator
for i in range(1,4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)    

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)


# Method 2: Using insert() method
# - append() only works for adding elements to the end of the list
# - to add an element to the desired position, insert() method is used
# - takes two args, (position, value)

# Complexities for Adding elements in a Lists(insert() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# Python program to demonstrate Addition of elements in a List
  
# Creating a List
List = [1,2,3,4]
print("\nInitial List: ")
print(List)
 
# Addition of Element at specific Position (using Insert Method)
List.insert(2, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)


# Method 3: Using extend() method
# - Other than append() and insert() methods, there’s one more method for the Addition of elements
# - extend() method is used to add multiple elements at the same time at the end of the list
# Note: append() and extend() methods can only add elements at the end

# Complexities for Adding elements in a Lists(extend() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# Python program to demonstrate addition of elements in a List
 
# Creating a List
List = [1, 2, 3, 4]
print("\nInitial List: ")
print(List)
 
# Addition of multiple elements to the List at the end (using Extend Method)
List.extend([8,'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
## Reversing a List

# Method 1: A list can be reversed using the reverse() method in python

myList = [1,2,3,4,'red','butterfly']
print("\ninitial list:")
print(myList)

myList.reverse()
print("\nreversed list (reverse() method):")
print(myList)

# Method 2: Using reversed() function:
# - reversed() function returns a reverse iterator, which can be converted to a list using the list() function.

myList2 = [1,2,3,4,5]
reversed_list = list(reversed(myList2))
print('\nreverese list using reversed() function')
print(reversed_list)
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
## Removing Elements from the List

# - Elements can be removed from the List by using the built-in remove() function
# - An Error arises if the element doesn’t exist in the list 
# - Remove() method only removes one element at a time
# - To remove a range of elements, the iterator is used 
# - The remove() method removes the specified item.

# Complexities for Deleting elements in a Lists(remove() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# Python program to demonstrate Removal of elements in a List
 
# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("\nInitial List: ")
print(List)

# Removing elements from List using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# Removing using iterator
# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Removing elements from List using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)


# Method 2: Using pop() function
# - pop() function can also be used to remove and return an element from the list
# - by default it removes only the last element of the list
# - to remove an element from a specific position of the List, index of the element is passed as argument to pop()

# Complexities for Deleting elements in a Lists(pop() method):
# Time Complexity: O(1)/O(n) (O(1) for removing the last element, O(n) for removing the first and middle elements)
# Space Complexity: O(1)

List = [1,2,3,4,5]

# removing element from set using pop()
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a specific location from the set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)

#------------------------------------------------------------------------------------------------------