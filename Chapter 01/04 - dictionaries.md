
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Dictionaries

Our little good reads collection is starting to look good and we can perform all kinds of manipulations on it. Now, imagine that our list is large and we would like to look up the score we gave to a particular book. How are we going to find that book? For this purpose Python provides another more appropriate data structure, named `dictionary`. A `dictionary` is similar to the dictionaries you have at home. It consists of entries, or keys, that hold a value. Let's define one:

```python runnable
my_dict = {"book": "physical objects consisting of a number of pages bound together",
           "sword": "a cutting or thrusting weapon that has a long metal blade",
           "pie": "dish baked in pastry-lined pan often with a pastry top"}

print(my_dict)
```

Take a close look at the new syntax. Notice the curly brackets and the colons. Keys are located at the left side of the colon; values at the right side. To look up the value of a given key, we 'index' the dictionary using that key:

```python runnable
my_dict = {"book": "physical objects consisting of a number of pages bound together",
           "sword": "a cutting or thrusting weapon that has a long metal blade",
           "pie": "dish baked in pastry-lined pan often with a pastry top"}

description = my_dict["sword"]
print(description)
```

We say 'index', because we use the same syntax with square brackets when indexing lists or strings. The differences is that we don't use a position number to index a dictionary, but a key. Like lists, dictionaries are mutable which means we can add and remove entries from it. Let's define an empty dictionary and add some books to it. The titles will be our keys and the scores their values. Watch the syntax to add a new entry:

```python runnable
good_reads = {}
good_reads["Pride and Prejudice"] = 8
good_reads["A Clockwork Orange"] = 9

print(good_reads)
```

In a way this is similar to what we have seen before when we altered our book `list`. There we indexed the list using a integer to access a particular book. Here we directly use the title of the book. Can you imagine why this is so useful?

# Quiz!

Update the new good reads datastructure with your own books. Try to print out the score you gave for one of the books.

```python runnable
# insert your code here
```

# keys(), values()

To retrieve a list of all the books we have in our collection, we can ask the dictionary to return its keys as a list:

```python
good_reads.keys()
```

Similarly we can ask for the values:

```python
good_reads.values()
```

# What we have learnt

To finish this section, here is an overview of the new concepts and functions you have learnt. Make sure you understand them all.

* dictionary
* indexing or accessing keys of dictionaries
* adding items to a dictionary
* `.keys()`
* `.values()`

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
