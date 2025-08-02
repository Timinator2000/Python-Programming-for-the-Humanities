
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Writing our first function

In the previous quiz, you probably wrote a loop that iterates over all characters in `text` and adds 1 to `number_of_es` each time the program finds the letter _e_. Counting objects in a text is a very common thing to do. Therefore, Python provides the convenient function `count`. This function operates on strings (`somestring.count(argument)`) and takes as argument the object you want to count. Using this function, the solution to the quiz above can now be rewritten as follows:

```python
number_of_es = text.count("e")
print(number_of_es)
```

In fact, `count` takes as argument any string you would like to find. We could just as well count how often the determiner `an` occurs:

```python
print(text.count("an"))
```

The string `an` is found 12 times in our text. Does that mean that the word _an_ occurs 12 times in our text? Go ahead. Count it yourself. In fact, an occurs only twice... Think about this. Why does Python print 12?

If we want to count how often the word _an_ occurs in the text and not the string `an`, we could surround _an_ with spaces, like the following:

```python
print(text.count(" an "))
```

Although it gets the job done in this particular case, it is generally not a very solid way of counting words in a text. What if there are instances of _an_ followed by a semicolon or some end-of-sentence marker? Then we would need to query the text multiple times for each possible context of _an_. For that reason, we're going to approach the problem using a different, more sophisticated strategy.

Recall from the previous chapter the function `split`. What does this function do? The function `split` operates on a string and splits a string on spaces and returns a list of smaller strings (or words):

```python
print(text.split())
```

# Quiz!

All the things you have learnt so far should enable you to write code that counts how often a certain item occurs in a list. Write some code that defines the variable `number_of_hits` and counts how often the word `in` (assigned to `item_to_count`) occurs in the the list of words called `words`.

```python
words = text.split()
number_of_hits = 0
item_to_count = "in"
# insert your code here

# The following test should print True if your code is correct 
print(number_of_hits == 3)
```

We will go through the previous quiz step by step. We would like to know how often the preposition _in_ occurs in our text. As a first step we will split the string text into a list of words:

```python
words = text.split()
```

Next we define a variable `number_of_hits` and set it to zero.

```python
number_of_hits = 0
```

The final step is to loop over all `words` in words and add 1 to `number_of_hits` if we find a word that is equal to _in_:

```python
item_to_count = "in"
for word in words:
    if word == item_to_count:
        number_of_hits += 1
print(number_of_hits)
```

Now, say we would like to know how often the word _of_ occurs in our text. We could adapt the previous lines of code to search for the word _of_, but what if we also would like to count the number of times _the_ occurs, and _house_ and _had_ and... It would be really cumbersome to repeat all these lines of code for each particular search term we have. Programming is supposed to reduce our workload, not increase it. Just like the function `count` for strings, we would like to have a function that operates on lists, takes as argument the object we would like to count and returns the number of times this object occurs in our list.

In this and the previous chapter you have already seen lots of functions. A function does something, often based on some argument you pass to it, and generally returns a result. You are not just limited to using functions in the standard library but you can write your own functions.

In fact, you _must_ write your own functions. Separating your problem into sub-problems and writing a function for each of those is an immensely important part of well-structured programming. Functions are defined using the `def` keyword, they take a name and optionally a number of parameters.

```python
def some_name(optional_parameters):
```

The `return` statement returns a value back to the caller and always ends the execution of the function.

Going back to our problem, we want to write a function called `count_in_list`. It takes two arguments: (1) the object we would like to count and (2) the list in which we want to count that object. Let's write down the function definition in Python:

```python
def count_in_list(item_to_count, list_to_search):
```

Do you understand all the syntax and keywords in the definition above? Now all we need to do is to add the lines of code we wrote before to the body of this function:

```python
def count_in_list(item_to_count, list_to_search): 
    number_of_hits = 0                            
    for item in list_to_search:                   
        if item == item_to_count:                 
            number_of_hits += 1                   
    return number_of_hits                         
```

All code should be familiar to you, except the `return` keyword. The `return` keyword is there to tell python to return as a result of calling the function the argument `number_of_hits`. OK, let's go through our function one more time, just to make sure you really understand all of it.

1. First we define a function using `def` and give it the name `count_in_list` (line 1);
1. This function takes two arguments: `item_to_count` and `list_to_search` (line 1);
1. Within the function, we define a variable `number_of_hits` and assign to it the value zero (since at that stage we haven't found anything yet (line 2));
1. We loop over all words in `list_to_search` (line 3);
1. If we find a word that is equal to `item_to_count` (line 4), we add 1 to `number_of_hits` (line 5);
1. Return the result of `number_of_hits` (line 6).

Let's test our little function! We will first count how often the word _an_ occurs in our list of words `words`.

```python
print(count_in_list("an", words))
```

# Quiz!

Using the function we defined, print how often the word the occurs in our text

```python
# insert your code here
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
