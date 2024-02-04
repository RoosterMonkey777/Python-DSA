# Remove character in a String except Alphabet

# Given a string consisting of alphabets and other characters, remove all the characters other than alphabets and print the string so formed.

# Example
# Input: str = "$Gee*k;s..fo, r'Ge^eks?"
# Output: GeeksforGeeks

# Program to Remove characters in a string except alphabets

# Below are the steps and methods by which we can remove all characters other than alphabets using List Comprehension and ord() in Python:
# - Using ord() and range()
# - Using filter() and lambda
# - Using isalpha()

# Remove All Characters Other Than Alphabets using ord() and range()
# The ord() method returns an integer representing the Unicode code point of the given Unicode character. For example,
# ord('5') = 53 and ord('A') = 65 and ord('$') = 36

def removeAll(input): 
    # Traverse complete string and separate all characters which lies between [a-z] or [A-Z] 
    sepChars = [char for char in input if ord(char) in range(ord('a'),ord('z')+1,1) or ord(char) in range(ord('A'),ord('Z')+1,1)] 
    # join all separated characters and print them together 
    return ''.join(sepChars) 
 
# Driver program 
if __name__ == "__main__": 
    input = "$Gee*k;s..fo, r'Ge^eks?"
    print (removeAll(input))


# Python Remove All Characters Using filter() and lamda
# In this example, we are using filter() and lambda to remove all characters other than alphabets.
string = "$Gee*k;s..fo, r'Ge^eks?"
print("".join(filter(lambda x : x.isalpha(),string)))