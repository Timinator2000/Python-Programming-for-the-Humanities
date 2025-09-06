
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Inheritance *

One of the neat things you can do with classes is that you can build more specialised classes on top of more generic classes. `Person` for instance is a rather generic concept. We can use this generic class to build a more specialised class `Teacher`, a person that teaches a course. If you use inheritance, everything that the parent class could do, the inherited class can do as well!

The syntax for inheritance is as follows, do not confuse it with parameters in a function/method definition. We also add an extra method `stateprofession()` otherwise `Teacher` would be no different than `Person`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))

        
class Teacher(Person): #this class inherits the class above!
    def stateprofession(self):
        print("I am a teacher!")
```


```python
author = Teacher("Maarten",30)
author.introduceyourself()
author.stateprofession()
```

# Exercise

If the class `Person` would have already had a method `stateprofession`, then it would have been overruled (we say *overloaded*) by the one in the `Teacher` class. Edit the example above, add a print like *"I have no profession! :'("* and see that nothings changes

---

Instead of completely overloading a method, you can also call the method of the parent class. The following example contains modified versions of all methods, adds some extra methods and variables to keep track of the courses that are taught by the teacher. The edited methods call the method of the parent class the avoid repetition of code (one of the deadly sins of computer programming):


```python
class Teacher(Person): #this class inherits the class above!
    def __init__(self, name, age):
        self.courses = [] #initialise a new variable
        super().__init__(name,age) #call the init of Person
        
    def stateprofession(self):
        print("I am a teacher!")        
    
    def introduceyourself(self):
        super().introduceyourself() #call the introduceyourself() of the Person
        self.stateprofession()
        print("I teach " + str(self.nrofcourses()) + " course(s)")
        for course in self.courses:
            print("I teach " + course)
      
        
    def addcourse(self, course):
        self.courses.append(course)
        
    def nrofcourses(self):
        return len(self.courses)
    
    
author = Teacher("Maarten",30)
author.addcourse("Python")
author.introduceyourself()
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

