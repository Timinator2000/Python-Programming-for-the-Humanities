
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

<p style="font-size:20px; color:#FF3333; font-weight:bold;">Chapter is still in DRAFT stage</p>

---

# Chapter 6: Object-Oriented Programming

In this chapter we will introduce a new programming paradigm: **Object-Oriented Programming**. We will build an application that builds a social network and computes a graph of relations between people on Twitter. The nodes of the graph will be the twitter users, and the directed edges indicate that one speaks to another. The edges will carry a weight representing the number of times messages were sent. 

Given a twitter corpus, we will extract who talks to whom, and whenever a connection is found, an edge is added to our graph, or an existing edge is strenghtened.

Object-oriented programming is a data-centered programming paradigm that is based on the idea of grouping data and functions that act on particular data in so-called **classes**. A class can be seen as a complex data-type, a template if you will. Variables that are of that data type are said to be **objects** or **instances** of that class.

# An Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Ok, several things happen here. Here we created a class Person with a function `__init__`. Functions that start with underscores are always special functions to Python which are connected with other built-in aspects of the language. The initialisation function will be called when an object of that initialised. Let's do so:

```python
author = Person("Maarten", 30)
print("My name is " + author.name)
print("My age is " + str(author.age))
```

Functions within a class are called **methods**. The initialisation method assigns the two parameters that are passed to variables that *belong to the object*, within a class definition the object is always represented by `self`.

The first argument of a method is always `self`, and it will always point to the instance of the class. This first argument however is never explicitly specified when you call the method. It is implicitly passed by Python itself. That is why you see a discrepancy between the number of arguments in the instantiation and in the class definition.

Any variable or methods in a class can be accessed using the period (`.`) syntax:

    object.variable 

or:

    object.method



In the above example we printed the name and age. We can turn this into a method as well, thus allowing any person to introduce himself/herself. Let's extend our example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))
        
author = Person("Maarten",30)
author.introduceyourself()
```

Do you see what happens here? Do you understand the role of `self` and notation with the period?

Unbeknowst to you, we have already made use of countless objects and methods throughout this course. Things like strings, lists, sets, dictionaries are all objects! Isn't that a shock? 😀 The object oriented paradigm is ubiquitous in Python!

# Exercise

Add a variable `gender` (a string) to the Person class and adapt the initialisation method accordingly. Also add a method `ismale()` that uses this new information and returns a boolean value (True/False).

```python
#adapt the code:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))
        
author = Person("Maarten",30)
author.introduceyourself()
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

