
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Simple Conditions

A lot of programming has to do with executing a certain piece of code if a particular condition holds. We have already seen two conditions at the very beginning of the chapter. Here we give a brief overview. Can you figure out what all of the conditions do?

```python runnable
print("2 < 5 =", 2 < 5)
print("3 > 7 =", 3 > 7)
print("3 == 4 =", 3 == 4)
print("school == homework =", "school" == "homework")
print("Python != perl =", "Python" != "perl")
```

# if, elif and else

The dictionary is a much better data structure for our good reads collections. However, even with dictionaries we might forget which books we added to the collection. What happens if we try to get the score of a book that is not in our collection (and hopefully never will be...)?

```python runnable
good_reads = {"Pride and Prejudice": 8, "A Clockwork Orange": 9}

print(good_reads["Folgert's awesomeness"])
```

We get an error. A `KeyError`, which basically means "the key you asked me to look up is not in the dictionary". We will learn a lot more about error handling later, but for now we would like to prevent our program from giving it in the first place. Let's write a little program that prints "X is in the collection" if a particular book is in the collection and "X is NOT in the collection" if it is not.

```python runnable
good_reads = {"Pride and Prejudice": 8, "A Clockwork Orange": 9}

book = "A Clockwork Orange"
if book in good_reads:
    print(book + " is in the collection")
else:
    print(book + " is NOT in the collection")
```

A lot of new syntax here. Let's go through it step by step. First we ask if the value we assigned to `book` is in our collection. The part after `if` evaluates to either `True` or to `False`. Let's type that in:

```python runnable
good_reads = {"Pride and Prejudice": 8, "A Clockwork Orange": 9}

book = "The Hunger Games"
print(book in good_reads)
```

Because our book is not in the collection, Python returns `False`. Let's do the same thing for a book that we know is in the collection:

```python runnable
good_reads = {"Pride and Prejudice": 8, "A Clockwork Orange": 9}

print("A Clockwork Orange" in good_reads)
```

Indeed, it is in the collection. Back to our `if` statement. If the expression after `if` evaluates to `True`, our program will go on to the next line and print `book + " is in the collection"`. Let's try that as well:

```python runnable
good_reads = {"Pride and Prejudice": 8, "A Clockwork Orange": 9}

if "A Clockwork Orange" in good_reads:
    print("Found it!")

book = "The Hunger Games"
if book in good_reads:
    print("Found it!")
```

Notice that the print statement in the last code block is not executed. That is because the value we assigned to `book` is not in our collection and thus the part after `if` did not evaluate to `True`. In our little program above we used another statement besides `if`, namely `else`. It shouldn't be too hard to figure out what's going on here. The part after `else` will be executed if the `if` statement evaluated to `False`. In English: if the book is not in the collection, print that it is not.

# Indentation!

Before we continue, we must first explain to you that the layout of our code is not optional. Unlike in other languages, Python does not make use of curly braces to mark the start and end of expressions. The only delimiter is a colon (`:`) and the indentation of the code. This indentation must be used consistently throughout your code. The convention is to use 4 spaces as indentation. This means that after you have used a colon (such as in our `if` statement) the next line should be indented by four spaces more than the previous line.

Sometimes we have various conditions that should all evaluate to something different. For that Python provides the `elif` statement. We use it similar to `if` and `else`. Note however that you can only use `elif` after an `if` statement! Above we asked whether a book was in the collection. We can do the same thing for parts of strings or for items in a list. For example we could test whether the letter _a_ is in the word _banana_:


```python runnable
print("a" in "banana")
```

Likewise the following evaluates to `False`:

```python runnable
print("z" in "banana")
```

Let's use this in an `if-elif-else` combination:

```python runnable
word = "rocket science"

if "a" in word:
    print(word + " contains the letter a")
elif "s" in word:
    print(word + " contains the letter s")
else:
    print("What a weird word!")
```

# Quiz!

Let's practice our new condition skills a little. Write a small program that defines a variable `weight`. If the weight is > 50 pounds, print "There is a $25 charge for luggage that heavy." If it is not, print: "Thank you for your business." Change the value of weight to see both statements. (Tip: make use of the `<` or `>` operators)

```python runnable
# insert your code here
```

# and, or, not

Up to this point, our conditions have consisted of single expressions. However, quite often we would like to test for multiple conditions and then execute a particular piece of code. Python provides a number of ways to do that. The first is with the `and` statement. `and` allows us to juxtapose two expressions that need to be true in order to make the entire expression evaluate to `True`. Let's see how that works:

```python runnable
word = "banana"

if "a" in word and "b" in word:
    print("Both a and b are in " + word)
```

If one of the expressions evaluates to `False`, nothing will be printed:

```python runnable
word = "banana"

if "a" in word and "z" in word:
    print("Both a and z are in " + word)
```

# Quiz!

Replace `and` with `or` in the `if` statement below. What happens?

```python runnable
word = "banana"

if "a" in word and "z" in word:
    print("Both a and b are in " + word)
```

In the code block below, can you add an `else` statement that prints that none of the letters were found?

```python runnable
word = "banana"

if "a" in word and "z" in word:
    print("Both a and z are in " + word)
# insert your code here
```

Finally we can use `not` to test for conditions that are not true.

```python runnable
word = "banana"

if "z" not in word:
    print("z is not in " + word)
```

Objects, such as strings or integers or lists are `True` because they exist. Empty strings, lists, dictionaries etc on the other hand are `False` because in a way they do not exist. We can use this principle to, for example, only execute a piece of code if a certain list contains any values:

```python runnable
numbers = [1, 2, 3, 4]

if numbers:
    print("I found some numbers!")
```

Now if our list were empty, Python wouldn't print anything:

```python runnable
numbers = []

if numbers:
    print("I found some numbers!")
```

# Quiz!

Can you write code that prints "This is an empty list" if the provided list does not contain any values?

```python runnable
numbers = []

# insert your code here
```

Can you do the same thing, but this time using the function `len()`?

```python runnable
numbers = []

# insert your code here
```

# What we have learnt

To finish this section, here is an overview of the new functions, statements and concepts we have learnt. Go through them and make sure you understand what their purpose is and how they are used.

* conditions
* indentation
* `if`
* `elif`
* `else`
* `True`
* `False`
* empty objects are false
* `not`
* `in`
* `and`
* `or`
* multiple conditions
* `==`
* `<`
* `>`
* `!=`
* `KeyError`

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)
