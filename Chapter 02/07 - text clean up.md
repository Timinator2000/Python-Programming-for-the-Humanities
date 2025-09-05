
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Text clean up

In the previous section we wrote code to compute a frequency distribution of the words in a text stored on our computer. The function `split` is a quick and dirty way of splitting a string into a list of words. However, if we look through the frequency distributions, we notice quite an amount of noise. For instance, the pronoun _her_ occurs 4 times, but we also find `her.` occurring 1 time and the capitalized `Her`, also 1 time. Of course we would like to add those counts to that of _her_. As it appears, the tokenization of our text using `split` is fast and simple, but it leaves us with noisy and incorrect frequency distributions.

There are essentially two strategies to follow to correct our frequency distributions. The first is to come up with a better procedure of splitting our text into words. The second is to clean-up our text and pass this clean result to the convenient `split` function. For now we will follow the second path.

Some words in our text are capitalized. To lowercase these words, Python provides the function `lower`. It operates on strings:

```python runnable
x = 'Emma'
x_lower = x.lower()
print(x_lower)
```

We can apply this function to our complete text to obtain a completely lowercased text, using:

```python runnable
text_lower = text.lower()
print(text_lower)
```

This solves our problem with miscounting capitalized words, leaving us with the problem of punctuation. The function `replace` is just the function we're looking for. It takes two arguments: (1) the string we would like to replace and (2) the string we want to replace the first argument with:

```python runnable
x = 'Please. remove. all. dots. from. this. sentence.'
x = x.replace(".", "")
print(x)
```

Notice that we replace all dots with an empty string written as `""`.

# Quiz!

Write code to lowercase and remove all commas in the following short text:

```python runnable
short_text = "Commas, as it turns out, are so much overestimated."
# insert your code here

# The following test should print True if your code is correct 
print(short_text == "commas as it turns out are so much overestimated.")
```

We would like to remove all punctuation from a text, not just dots and commas. We will write a function called `remove_punc` that removes all (simple) punctuation from a text. Again, there are many ways in which we can write this function. We will show you two of them. The first strategy is to repeatedly call `replace` on the same string each time replacing a different punctuation character with an empty string.

```python runnable
def remove_punc(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        text = text.replace(marker, "")
    return text


short_text = "Commas, as it turns out, are overestimated. Dots, however, even more so!"
print(remove_punc(short_text))
```

The second strategy we will follow is to show you that we can achieve the same result without using the built in function `replace`. Remember that a string consists of characters. We can loop over a string accessing each character in turn. Each time we find a punctuation marker we skip to the next character.

```python runnable
def remove_punc2(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    clean_text = ""
    for character in text:
        if character not in punctuation:
            clean_text += character
    return clean_text

short_text = "Commas, as it turns out, are overestimated. Dots, however, even more so!"
print(remove_punc2(short_text))
```

# Quiz!

1. Can you come up with any pros or cons for each of the two functions above?

1. Now it is time to put everything together. We want to write a function `clean_text` that takes as argument a text represented by string. The function should return this string with all punctuation removed and all characters lowercased.

    ```python runnable
    def clean_text(text):
        # insert your code here
        
    # The following test should print True if your code is correct 
    short_text = "Commas, as it turns out, are overestimated. Dots, however, even more so!"
    print(clean_text(short_text) == 
        "commas as it turns out are overestimated dots however even more so")
    ```

1. This last excercise puts everything together. We want you to open and read the file `data/austen-emma.txt` text once more, clean up the text and recompute the frequency distribution. Assign to `woodhouse_counts` the number of times the name Woodhouse occurs in the text.

    ```python runnable
    woodhouse_counts = 0
    # insert your code here

    # The following test should print True if your code is correct 
    print(woodhouse_counts == 263)
    ```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)
