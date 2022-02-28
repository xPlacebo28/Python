# Subject: Types of Variables in Python
# Date: 2/28/22

############################################################
# Strings (immutable Python objects)
############################################################
#
# A string is a sequence of characters. It can be declared 
# in python by using double-quotes. Strings are immutable, 
# i.e., they cannot be changed.

# Assigning string to a variable
a = "This is a string"
print (a)


############################################################
# Lists (mutable Python objects)
############################################################

# Lists are one of the most powerful tools in python. 
# They are just like the arrays declared in other languages. 
# But the most powerful thing is that list need not be always 
# homogeneous. A single list can contain strings, integers, as 
# well as objects. Lists can also be used for implementing 
# stacks and queues. Lists are mutable, i.e., they can be 
# altered once declared.

# Declaring a list
L = [1, "a" , "string" , 1+2]
print L
L.append(6)
print L
L.pop()
print L
print L[1]


############################################################
# Tuples (immutable Python objects -- Very fast)
############################################################

# A tuple is a sequence of immutable Python objects. 
# Tuples are just like lists with the exception that tuples 
# cannot be changed once declared. Tuples are usually faster 
# than lists.


tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])






