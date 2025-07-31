
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

<BR>

```python runnable
print("Ready, set, GO!")
```

Everyone can learn how to program and the best way to learn is by doing. In this tutorial you will be asked to write a lot of code. [Click run below any code block to execute the code shown.] Let's begin right away and write our first little program!


# Quiz!

In the code box below, write a simple program that calculates how many minutes there are in seven weeks.

>Playground note: you must put your calculation inside a print statement like this:

```python
print(3+4)
```

```python runnable
print()
```

Great! You have written your first little program and you've done it without any help! So, can we now go beyond using our programming language as a simple calculator? Before we ask you to write another program, we will first have to explain something about 'assignment'.

We can assign values to variables using the `=` operator. A variable is just a name we give to a particular value, you can imagine it as a box you put a certain value into, and on which you write a name with a black marker. The following code block contains two operations. First, we assign the value 2 to the name `x`. After that `x` will hold the value 2. You might say Python stored the value 2 in `x`. Finally we print the value using the `print()` command.

```python runnable
x = 2
print(x)
```

Now that we stored the value 2 in `x`, we can use the variable `x` to do things like the following:

```python runnable
x = 2
print(x * x)
print(x == x)
print(x > 6)
```

Can you figure out what is happening here?

Variables are not just numbers. They can also be text. These are called strings. For example:

```python runnable
book = "The Lord of the Flies"
print(book)
```

A string in Python must be enclosed with quotes (either single or double quotes). Without those quotes Python thinks its dealing with variables that have been defined earlier. `book` is a variable to which we assign the string `"The Lord of the Flies"`, but that same string is not a variable but a value!

Variable names can be chosen arbitrarily. We give a certain value a name, and we are free to pick one to our liking. It is, however, recommended to use senseful names as we will use the variable names in our code directly and not the values they hold.

```python runnable
# not recommended...
banana = "The Lord of the Flies"
print(banana)
```

You are free to use the name `banana` to hold the title `"The Lord of the Flies"` but you will agree that this naming is not transparent.

Variables can vary and we can update our variables. Say we have counted how many books we have in our office:

```python
number_of_books = 100
```

Then, when we obtain a new book, we can update the number of books accordingly:

```python runnable
number_of_books = 100

number_of_books = number_of_books + 1
print(number_of_books)
```

Updates like these happen a lot. Python therefore provides a shortcut and you can write the same thing using `+=`:

```python runnable
number_of_books = 100

number_of_books = number_of_books + 1
number_of_books += 5
print(number_of_books)
```

For now the final interesting thing we would like to mention about variables is that we can assign the value of one variable to another variable. We will explain more about this later on, but here you just need to understand the basic mechanism. Before you evaluate the following code block, can you predict what Python will print?

```python runnable
book = "The Lord of the Flies"
reading = book
print(reading)
```

# Quiz!

Now that you understand all about assigning values to variables, it is time for our second programming quiz. We want you to write some code that defines a variable, name, and assign to it a string that is your name. If your first name is shorter than 5 characters, use your last name. If your last name is also shorter than 5 characters, use the combination of you first and last name.

```python runnable
# insert your code here
print(name)
```

# What we have learnt

To finish this section, here is an overview of the concepts you have learnt. Go through the list and make sure you understand all the concepts.

* variable
* value
* assignment to variables
* difference between variables and values
* strings
* integers
* varying variables
