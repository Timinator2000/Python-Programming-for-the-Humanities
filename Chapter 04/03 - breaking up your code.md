
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Breaking up your code

Another important aspect of good programs is reusability. It is good practice to write general functions that can be applied to a range of problems which you can combine into a complex of functions for a particular task. Again, this can best be shown with an example. 

We will write  two versions of a program to transform an English word into [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin). To translate an English word into Pig Latin we apply the following rules:

-  If a word begins with a consonant or consonant cluster, remove that part from the beginning of the word and add it to the end of the word. Now to make it really latinish, add "ay" to this. E.g. *duck* - *uckday* and *bush* - *ushbay*.
-  If a word starts with a vowel, simply add "ay" to the end of the word. E.g. *egg* - *eggay* and *inbox* - *inboxay*.

We will first give you a rather verbose function that does it all in one shot:


```python
def translate(word):
    "Convert a word to latin."
    vowels = 'aeiouAEIOU'
    start = 0
    end = ''
    # loop over all characters in word
    for i, char in enumerate(word):
        # if this character is not a vowel
        if char not in vowels:
            # it is a consonant, so add it to the end.
            end += char
        # if it is a vowel
        else:
            # we set the starting position to 
            # the position of this character
            start = i
            break
    return word[start:] + end + 'ay'
```

From just looking at this function it is hard to see what it is doing exactly. We'll try to explain it. It loops over each character in `word` and for each character it asks whether it is not a vowel (i.e. a consonant). If it is a consonant, we add it to the `end` variable which we will later append to the remaining word. While this is `True` we carry on to the next character. If we find a vowel, we store the index of that vowel and `break` from the loop. Now we return the word starting from the first vowel found, add the consonant or conconant cluster to it and add *ay* to that word.

Okay, so this works, but it is not very readable, now is it? If you have a particular problem, it is good practice to divide it into subproblems and solve them separately. Let's break this function up into more comprehensible parts. First we will write a function called `starts_with_vowel`, which takes as argument a string and returns if the first character is a vowel.

# Quiz!

Define a function called `starts_with_vowel` which takes as argument a word represented by a string. The function should return `True` if the word starts with a vowel; `False` otherwise.

```python
# write your code here

# do not modify the code below, it is for testing your answer only!
# it should output True if you did well
print(starts_with_vowel("egg") == True)
print(starts_with_vowel("bacon") == False)
```

---

One possible way to write the function `starts_with_vowel` is the following:


```python
def starts_with_vowel(word):
    "Return True if WORD starts with a vowel, False otherwise."
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return word.startswith(vowels)
```

In the function `starts_with_vowel` we define a variable `vowels` which is a tuple containing all vowels, both uppercase and lowercase. We then call the built in function `startswith` which operates on strings and takes as argument either a string or a tuple of strings. It checks for each item in the tuple whether the string starts with that item. As soon as it finds one, it returns `True`. If the string does not start with any of the items in the tuple, it will return `False`.

Perhaps someday we would like add different Latin endings to words. Having to change *ay* directly in our code for each suffix we choose is rather inconvenient. 

# Quiz!

Write a function called `add_suffix`. It takes as argument two strings: a word and the string we would like to attach to that word.


```python
def add_suffix(word, suffix):
    "Return WORD with SUFFIX attached."
    # insert your code here
    
# do not modify the code below, it is for testing your answer only!
# it should output True if you did well
print(add_suffix("egg", "ay") == "eggay")
print(add_suffix("egg", "oing") == "eggoing")
```

---

If we really want a separate function to add *ay* to words, we can now define it as follows:


```python
def add_ay(word):
    "Return WORD with 'ay' attached."
    return add_suffix(word, "ay")
```

This is a small and a little silly example of how we can recombine and reuse functions into other more specific functions. Now that we have defined these small helper functions, have a look at the following implementation of `translate`:


```python
def translate(word, suffix):
    if starts_with_vowel(word):
        return add_suffix(word, suffix)
    return translate(word[1:] + word[0], suffix)
```

The first thing we notice is that this definition is much shorter. This function provides a recursive solution to our problem and can be read as follows: if the input word starts with a vowel, return the word and add *ay* to it. If it does not start with a vowel, move the first character to the end of the word and try to convert it once more. In our - perhaps subjective - opinion, the recursive solution provides a much more elegant solution to our problem.

The function `translate` is a reusable function, independent of the suffix we choose. The following function makes use of the generic nature of `translate` and defines a translation function specific to pig latin:


```python
def pig_latinize(word):
    "Pig latinize WORD."
    return translate(word, "ay")
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

