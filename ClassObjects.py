# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:53:34 2022

@author: zyoas
"""

# Class objects support two kinds of operations: attribute references and instantiation
# Attribute references use the standard syntax used for all attribute references 
# in Python: obj.name. Valid attribute names are all the names that were in the 
# class’s namespace when the class object was created. So, if the class 
# definition looked like this:

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
# then MyClass.i and MyClass.f are valid attribute references, returning an 
# integer and a function object, respectively. Class attributes can also be 
# assigned to, so you can change the value of MyClass.i by assignment. __doc__ 
# is also a valid attribute, returning the docstring belonging to the 
# class: "A simple example class".

# Class instantiation uses function notation. Just pretend that the class 
# object is a parameterless function that returns a new instance of the class.
# For example:

x = MyClass()

# The instantiation operation (“calling” a class object) creates an empty 
# object. Many classes like to create objects with instances customized to a 
# specific initial state. Therefore a class may define a special method named
#  __init__(), like this:

def __init__(self):
    self.data = []

# When a class defines an __init__() method, class instantiation automatically
# invokes __init__() for the newly-created class instance. So in this example,
# a new, initialized instance can be obtained by:

x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility.
# In that case, arguments given to the class instantiation operator are passed 
# on to __init__(). For example,

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

# Taken from official documentation which helped me the most in the end.

# Here is my example

class Bill():
    def __init__(self,apples,figs,dates):
        self.apples = apples
        self.figs = figs
        self.dates = dates
        self.bill = apples + figs + dates
        print ("Buy",self.apples,"apples", self.figs,"figs 
                and",self.dates,"dates. 
                Total fruitty bill is",self.bill," pieces of fruit :)")

# When you create instance of class Bill:

purchase = Bill(5,6,7)

# You get:

> Buy 5 apples 6 figs and 7 dates. Total fruitty bill is 18  pieces of
> fruit :)
