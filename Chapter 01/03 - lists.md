
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Lists

Consider the sentence below:

```python
sentence = "Python's name is derived from the television series Monty Python's Flying Circus."
```

<BR>

Words are made up of characters, and so are string objects in Python. As we will see, it is always to be prefered to represent our data as naturally as possible. Now for the sentence above, it seems more natural to describe it in terms of words than in terms of characters. Say we want to access the first word in our sentence. If we type in:

```python runnable
sentence = "Python's name is derived from the television series Monty Python's Flying Circus."

first_word = sentence[0]
print(first_word)
```

<BR>

Python only prints the first letter of our sentence. (Think about this if you do not understand why.) We can transform our sentence into a `list` of words (represented by strings) using the `split()` function as follows:

```python runnable
sentence = "Python's name is derived from the television series Monty Python's Flying Circus."

words = sentence.split()
print(words)
```

<BR>

By issuing the function split on our sentence, Python splits the sentence on spaces and returns a list of words. In many ways a list functions like a string. We can access all of its components using indexes and we can use slice indexes to access parts of the list. Let's try it!

# Quiz!

Write a small program that defines a variable `first_word` and assign to it the first word of our word list. Play around a little with the indexes to see if you really understand how it works.

```python runnable
sentence = "Python's name is derived from the television series Monty Python's Flying Circus."

first_word = # insert your code here
print(first_word)
```

<BR>

A `list` acts like a container where we can store all kinds of information. We can access a list using indexes and slices. We can also add new items to a list. For that you use the method `append`. Let's see how it works. Say we want to keep a list of all our good reads. We start with an empty list and we will add some good books to it:

```python runnable
#start with an empty list
good_reads = []
good_reads.append("The Hunger Games")
good_reads.append("A Clockwork Orange")
print(good_reads)
```

Now, if for some reason we don't like a particular book anymore, we can change it as follows:

```python runnable
good_reads = ["The Hunger Games", "A Clockwork Orange"]

good_reads[0] = "Pride and Prejudice"
print(good_reads)
```

<BR>

# Quiz!

Here's another small Quiz! Try to change the title of the second book in our good reads collection.

```python runnable
good_reads = ["Pride and Prejudice", "A Clockwork Orange"]

# insert your code here
print(good_reads)
```

<BR>

We just changed one element in a list. Note that if you do the same thing for a string, you will get an error:

```python runnable
name = "Pythen"
name[4] = "o"
```

<BR>

This is because `strings` (and some other types) are _immutable_. That is, they cannot be changed, as opposed to `lists` which are mutable. Let's explore some other ways in which we can manipulate lists.

# remove()

Let's assume our good read collection has grown a lot and we would like to remove some of the books from the list. Python provides the method `remove` that acts upon a list and takes as its argument the items we would like to remove.

```python runnable
good_reads = ["The Hunger Games", "A Clockwork Orange", 
              "Pride and Prejudice", "Water for Elephants",
              "The Shadow of the Wind", "Bel Canto"]

good_reads.remove("Water for Elephants")

print(good_reads)
```

<BR>

If we try to remove a book that is not in our collection, Python raises an error (don't be afraid, your computer won't break 😉).

```python runnable
good_reads = ["The Hunger Games", "A Clockwork Orange", 
              "Pride and Prejudice", "Water for Elephants",
              "The Shadow of the Wind", "Bel Canto"]

good_reads.remove("White Oleander")
```

<BR>

# Quiz!

Define a variable `good_reads` as an empty list. Now add some of your favorite books to it (at least three) and print the last two books you added.

```python runnable
# insert your code here
```

<BR>

Just as with strings, we can concatenate two lists. Here is an example:

```python runnable
# first we specify two lists of strings:
good_reads = ["The Hunger games", "A Clockwork Orange", 
              "Pride and Prejudice", "Water for Elephants",
              "The Shadow of the Wind", "Bel Canto"]

bad_reads = ["Fifty Shades of Grey", "Twilight"]

all_reads = good_reads + bad_reads
print(all_reads)
```

<BR>

# sort()

It is always nice to organise your bookshelf. We can sort our collection with the following expression:

```python runnable
good_reads = ["The Hunger games", "A Clockwork Orange", 
              "Pride and Prejudice", "Water for Elephants",
              "The Shadow of the Wind", "Bel Canto"]

good_reads.sort()
print(good_reads)
```

<BR>

# nested lists

Up to this point, our lists only have consisted of strings. However, a list can contain all kinds of data types, such as integers and even lists! Do you understand what is happening in the following example?

```python runnable
nested_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(nested_list[0])
print(nested_list[0][0])
```

<BR>

We can put this to use to enhance our good read collection with a score for every book we have. An entry in our collection will consist of a score within the range of 1 and 10 and the title of our book. The first element is the title; the second the score: `[title, score]`.

```python runnable
# initialize an empty list
good_reads = []

# add two books to the list:

good_reads.append(["Pride and Prejudice", 8])
good_reads.append(["A Clockwork Orange", 9])
```

<BR>

# Quiz!

Update the `good_reads` collection with some of your own books and give them all a score. Can you print out the score you gave to the first book in the list? (Tip: you can pile up indexes)

```python runnable
# insert your code here
```

<BR>

# What we have learnt

To finish this section, here is an overview of the new concepts and functions you have learnt. Go through them and make sure you understand them all.

* list
* _mutable_ versus _immutable_
* `.split()`
* `.append()`
* nested lists
* `.remove()`
* `.sort()`

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
