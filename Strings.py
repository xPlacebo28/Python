# Subject: Learning about data types Strings
# Date: 2/28/22

# Source: https://www.geeksforgeeks.org/python-strings/

# Summary: In Python, Strings are arrays of bytes representing Unicode characters. 
# However, Python does not have a character data type, a single character is 
# simply a string with a length of 1. Square brackets can be used to access 
# elements of the string.

###################################################################
# Creating Strings
###################################################################
# Strings in Python can be created using single quotes or double quotes or even triple quotes. 

# Python Program for
# Creation of String
 
# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)
 
# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
 
# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
 
# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)


###################################################################
# Accessing elements within the string
###################################################################

# Use forward and backward indexing to access the script
 
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
 
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])


###################################################################
# String Slicing
###################################################################

# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
 
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])
 
# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2])

###################################################################
# Deleting characters within a string
###################################################################

# Python Program to Delete
# characters from a String
 
  
# ------------------ INCORRECT WAY ------------------------------#
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
 
# Deleting a character
# of the String
del String1[2]
print("\nDeleting character at 2nd Index: ")
print(String1)

# -------------------- CORRECT WAY ------------------------------#

input_str = "DivasDwivedi"
   
# Printing original string  
print ("Original string: " + input_str) 
   
result_str = "" 
   
for i in range(0, len(input_str)): 
    if i != 3: 
        result_str = result_str + input_str[i] 
   
# Printing string after removal   
print ("String after removal of i'th character : " + result_str)

# OR HERE'S ANOTHER METHOD

str = "Engineering"
   
 
print ("Original string: " + str) 
   
# Removing char at index 2 
# using join() + list comprehension 
res_str = ''.join([str[i] for i in range(len(str)) if i != 2]) 
   
 
print ("String after removal of character: " + res_str) 

########################################################
# Formating Strings (Binary, exponential, rounding)
########################################################

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)
 
# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)
 
# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)


########################################################
# Formating Strings (Part 2) -- Using the % operator for rounding for display
########################################################








