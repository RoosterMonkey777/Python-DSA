# List Comprehension

# - Used for creating new lists from other iterables like tuples, strings, arrays, lists, etc 
# - A list comprehension consists of brackets containing the expression, 
# - which is executed for each element along with the for loop to iterate over each element

# Here's a basic syntax of list comprehension:
# new_list = [expression for item in iterable if condition]
# - expression is the operation or transformation to be performed on each element.
# - item is the variable representing each element in the iterable.
# - iterable is any iterable object (e.g., list, tuple, set, string) that you want to iterate over.
# - condition (optional) is an expression that filters the elements. 
# - Only elements for which the condition evaluates to True will be included in the new list.

# Create a list of squares of numbers from 0 to 9 using list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Python program to demonstrate list comprehension in Python below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range (1,11) if x%2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []
 
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x**2)
 
print(odd_square)
# 