# Nested List Comprehensions in Python

# List Comprehension are one of the most amazing features of Python. 
# It is a smart and concise way of creating lists by iterating over an iterable object. 
# Nested List Comprehensions are nothing but a list comprehension within another list comprehension 
# which is quite similar to nested for loops.

# Syntax: new_list = [[expression for item in list] for item in list]

#-----------------------------------------------------------------------------------------------------
# Example 1: Creating a Matrix

# Without List Comprehension:
# In this example, a 5×5 matrix is created using a nested loop structure. 
# An outer loop iterates five times, appending empty sublists to the matrix, 
# while an inner loop populates each sublist with values ranging from 0 to 4, 
# resulting in a matrix with consecutive integer values.
matrix = []
for i in range(5):
    # append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

# Using List Comprehension
# The same output can be achieved using nested list comprehension in just one line. 
# In this example, a 5×5 matrix is generated using a nested list comprehension. 
# The outer comprehension iterates five times, representing the rows, 
# while the inner comprehension populates each row with values ranging from 0 to 4, 
# resulting in a matrix with consecutive integer values.
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# Example 2: Filtering a Nested List Using List Comprehension

# Without Using List Comprehension
# In this example, a nested loop traverses a 2D matrix, extracting odd numbers from Python list 
# within list and appending them to the list odd_numbers. 
# The resulting list contains all odd elements from the matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

odd_numbers = []
for row in matrix:
    for element in row:
        if element%2 !=0:
            odd_numbers.append(element)
print(odd_numbers)

# Using List Comprehension
# In this example, a list comprehension is used to succinctly generate the list odd_numbers by iterating 
# through the elements of a 2D matrix. Only odd elements are included in the resulting list, 
# providing a concise and readable alternative to the equivalent nested loop structure.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_numbers = [element for row in matrix for element in row if element%2!=0]
print(odd_numbers)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# Example 3: Flattening Nested Sub-Lists

# Without List Comprehension
# In this example, a 2D list named matrix with varying sublist lengths is flattened using nested loops. 
# The elements from each sublist are sequentially appended to the list flatten_matrix, resulting in a 
# flattened representation of the original matrix.
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = []
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)

# With List Comprehension
# Again this can be done using nested list comprehension which has been shown below. 
# In this example, a 2D list named matrix with varying sublist lengths is flattened using nested list comprehension. 
# The expression [val for sublist in matrix for val in sublist] succinctly generates a flattened list by sequentially 
# including each element from the sublists.
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# nested list compr to flatten a given 2d matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# Example 4: Manipulate String Using List Comprehension

# Without List Comprehension
# In this example, a 2D list named matrix containing strings is modified using nested loops. 
# The inner loop capitalizes the first letter of each fruit, and the outer loop constructs a new 2D list, 
# modified_matrix, with the capitalized fruits, resulting in a matrix of strings with initial capital letters
matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]
 
modified_matrix = []
for row in matrix:
    modified_row = []
    for fruit in row:
        modified_row.append(fruit.capitalize())
    modified_matrix.append(modified_row)
print(modified_matrix)

# With List Comprehension
# In this example, a 2D list named matrix containing strings is transformed using nested list comprehension. 
# The expression [[fruit.capitalize() for fruit in row] for row in matrix] efficiently generates a modified matrix 
# where the first letter of each fruit is capitalized, resulting in a new matrix of strings with initial capital letters.

matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]
modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]
print(modified_matrix)
#-----------------------------------------------------------------------------------------------------