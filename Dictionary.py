# Subject: Within this module we will learn about dictionaries
# Date: 2/28/2022
# Author: Zach

##############################################################
# Dictionaries are created using the curly brackets {} and separated by the comma
# The format is "key:value" and the key is unique
##############################################################

dict_sample = {}

# Integer keys
dict_sample = {1: 'mango', 2: 'pawpaw'}

# Mixed keys
dict_sample = {'fruit': 'mango', 1: [4, 6, 8]}

# Also can build dictionaries using the dict() method
dict_sample = dict({1:'mango', 2:'pawpaw'})

# Can also be created to form a sequence
dict_sample = dict([(1,'mango'), (2,'pawpaw')])

# Nesting Dictionaries
dict_sample = {1: {'student1' : 'Nicholas', 'student2' : 'John', 'student3' : 'Mercy'},
        2: {'course1' : 'Computer Science', 'course2' : 'Mathematics', 'course3' : 'Accounting'}}

##############################################################
# Accessing Data Within Dictionaries
##############################################################

# Here we access the model arguement of dictionary and print it
# "key:value"
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample["model"]
print(x)

##############################################################
# Adding Elements to Existing Dictionary
##############################################################
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
dict_sample["Capacity"] = "1800CC"
print(dict_sample)

##############################################################
# Creating new dictionary and adding elements
##############################################################
MyDictionary[0] = 'Apples'
MyDictionary[2] = 'Mangoes'
MyDictionary[3] = 20
print("\n3 elements have been added: ")
print(MyDictionary)

##############################################################
# Updating elements
##############################################################
dict_sample = {  
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

dict_sample["year"] = 2014
print(dict_sample)  

##############################################################
# Removing elements
##############################################################
dict_sample = {  
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
del dict_sample["year"]  
print(dict_sample) 

# Or alternatively using the "pop" function

dict_sample.pop("year")
print(dict_sample)

# Delete the last item inserted into the dictionary

dict_sample.popitem()
print(dict_sample)

# Delete all entries within the dictionary, but leave it in the workspace
dict_sample.clear()

# Copy a dictionary
x = dict_sample.copy()

# Creating an iterable object from the dictionary

for key, value in dict_sample.items():
  print(k,v)
  
# Also a "fromkeys()" method. Here we create a dictionary with 3 different keys populated with values of the same value
name = ('John','Nicholas','Mercy')
age = 25

dict_sample = dict.fromkeys(name,age)
print(dict_sample)

# Values does not need to be populated, so the syntax can read...
dict_sample = dict.fromkeys(name)
print(dict_sample)

# Suppose we have a pre-existing dictionary and want to a) check if the key is present, and if not append it to the current dictionary
dict_sample = {  
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

x = dict_sample.setdefault("color", "Gray")

print(x)  

# Extract dictionary keys
dict_sample = {  
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

x = dict_sample.keys()

print(x) 

# Often times this method is used to iterate through each key in your dictionar, like so
dict_sample = {  
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

for k in dict_sample.keys():  
  print(k)

