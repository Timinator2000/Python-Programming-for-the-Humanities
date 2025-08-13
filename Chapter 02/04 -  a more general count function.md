
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|


<BR>

Our function `count_in_list` is a concise and convenient piece of code allowing us to rapidly and without too much repitition count how often certain items occur in a given list. Now what if we would like to find out for all words in our text how often they occur. Then it would be still quite cumbersome to call our function for each unique word. We would like to have a function that takes as argument a particular list and counts for each unique item in that list how often it occurs. There are multiple ways of writing such a function. We will show you two ways of doing it.

# A count function (take 1)

In the previous chapter you have acquainted yourself with the `dictionary` structure. Recall that a dictionary consists of keys and values and allows you to quickly lookup a value. We will use a dictionary to write the function `counter` that takes as argument a list and returns a `dictionary` with `keys` for each unique item and `values` showing the number of times it occurs in the list. We will first write some code without the function declaration. If that works, we will add it, just as before, to the body of a function.

We start with defining a variable `counts` which is an empty dictionary:

```python
counts = {}
```

Next we will loop over all words in our list `words`. For each word, we check whether the dictionary already contains it. If so, we add 1 to its value. If not, we add the word to the dictionary and assign to it the value 1.

```python runnable
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)
```

If you don't remember anymore how dictionaries work, go back to the previous chapter and read the part about dictionaries once more.

Now that our code is working, we can add it to a function. We define the function `counter` using the `def` keyword. It takes one argument (`list_to_search`).

```python
def counter(list_to_search):                 
    counts = {}                              
    for word in list_to_search:              
        if word in counts:                   
            counts[word] = counts[word] + 1  
        else:                                
            counts[word] = 1                 
    return counts                            
```

Hopefully we are boring you, but let's go through this function step by step.

1. We define a function using `def` and give it the name `counter` (line 1);
1. This function takes a single argument `list_to_search` which is the list we want to search through (line 1);
1. Next we define a variable `counts` which is an empty dictionary (line 2);
1. We loop over all words in `list_to_search` (line 3);
1. If the word is already in `counts`, we look up its current value and add 1 to it (line 4-5);
1. If the word is not in `counts` (else clause), we add the word to the dictionary and assign it the value 1 (line 6-7);
1. Return the result of counts (line 8);

Let's try out our new function!

```python runnable
def counter(list_to_search):                 
    counts = {}                              
    for word in list_to_search:              
        if word in counts:                   
            counts[word] = counts[word] + 1  
        else:                                
            counts[word] = 1                 
    return counts                            

print(counter(words))
```

# Quiz!

Let's put some of the stuff we learnt so far together. What we want you to do is to read into Python the file `data/austen-emma.txt`, convert it to a list of words and assign to the variable `emma_count` how often the word Emma occurs in the text.

```python runnable
emma_count = 0
# insert you code here
```

```python
# The following test should print True if your code is correct 
print(emma_count == 481)
```

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
