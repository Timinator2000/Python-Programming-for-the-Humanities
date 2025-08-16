
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# A count function (take 2)

Let's train our function writing skills a little more. We are going to write another counting function, this time using a slightly different strategy. Recall our function `count_in_list`. It takes as argument a list and the item we want to count in that list. It returns the number of times this item occurs in the list. If we call this function for each unique word in `words`, we obtain a list of frequencies, quite similar to the one we get from the function `counter`. What would happen if we just call the function `count_in_list` on each word in `words`?

```python runnable
infile = open('data/austen-emma-excerpt.txt')
text = infile.read()
infile.close()
words = text.split()

for word in words:
    print(word, count_in_list(word, words))
```

As you can see, we obtain the frequency of each word token in `words`, where we would like to have it only for unique word forms. The challenge is thus to come up with a way to convert our list of words into a structure with solely unique words. For this Python provides a convenient data structure called `set`. It takes as argument some iterable (e.g. a list) and returns a new object containing only unique items:

```python runnable
x = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
unique_x = set(x)
print(unique_x)
```

Using `set` we can iterate over all unique words in our word list and print the corresponding frequency:

```python runnable
unique_words = set(words)
for word in unique_words:
    print(word, count_in_list(word, words))
```

We wrap the lines of code above into the function `counter2`:

```python runnable
def counter2(list_to_search):
    unique_words = set(list_to_search)
    for word in unique_words:
        print(word, count_in_list(word, list_to_search))
```

A final check to see whether our function behaves correctly:

```python runnable
counter2(words)
```

# Quiz!

We have written two functions `counter` and `counter2`, both used to count for each unique item in a particular list how often it occurs in that list. Can you come up with some pros and cons for each function? Why is `counter2` better than `counter` or why is `counter` better than `counter2`?

Double click this cell and write down your answer.



<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)
