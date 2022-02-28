# Subject: In this lesson we learn about data types: sets
# Date: 2/28/22

# Set is an unordered collection of data type that is iterable,
# mutable, and has no duplicate elements. The order of elements
# in a set is undefined though it may consist of various elements.

# The major advantage of using a set, as opposed to a list,
# is that it has a highly optimized method for checking
# whether a specific element is contained in the set. 

###################################################################
# Creating a set
###################################################################

set1 = set()
set1 = set("GreeksForGeeks")
print(set1)

# Create a set with the use of constructor 
# (Using object to store string)
String = 'GreeksForGeeks'
print("\nSet with the use of an Object: ")
print(set1)


# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

###################################################################
# Adding to a set
###################################################################
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
  
# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

###################################################################
# Accessing a list
###################################################################
# Creating a set
set1 = set(["Geeks", "For", "Geeks"])  # Here we create a list of values and then convert it to a set
print("\nInitial set")
print(set1)
  
# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
  
# Checking the element
# using in keyword
print("Geeks" in set1)




