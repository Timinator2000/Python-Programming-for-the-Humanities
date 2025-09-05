
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Automatic Readability Index

The *Automatic Readability Index* is a readability test designed to gauge the understandability of a text. The formula for calculating the *Automated Readability Index* is as follows:

<BR>

![Automatic Readability Index](AutomaticReadabilityIndexFormula.png)

<BR>

Let's apply some wishful thinking. If we had all the information needed to compute this formula, we could start with writing a function that does it for us. Let's do so.

# Quiz!

Write a function `automatic_readability_index` that takes three arguments `n_chars`, `n_words` and `n_sents` and returns the ARI given those arguments.


```python
def automatic_readability_index(n_chars, n_words, n_sents):
    # insert your code here

# do not modify the code below, it is for testing your answer only!
# it should output True if you did well
print(abs(automatic_readability_index(300, 40, 10) - 15.895) < 0.001)
```

---------

Now we need to write some code to obtain the numbers we so wishfully assumed to have. We will use the code we wrote in earlier chapters to read and tokenise texts. In the file `preprocessing.py` we defined a function `read_corpus` which reads all files with the extension `.txt` in the given directory. It tokenizes each text into a list of sentences, each of which is represented by a list of words. All words are lowercased and we remove all punctuation. We import the function using the following line of code:


```python
from pyhum.preprocessing import read_corpus
```

Let's write a function `extract_counts` that takes a list of sentences as input and returns the number of characters, the number of words and the number of sentences as a tuple.

# Quiz!

Write the function `extract_counts`.


```python
def extract_counts(sentences):
    # insert your code here

# do not modify the code below, for testing only!
print(extract_counts(
    [["this", "was", "rather", "easy"], 
     ["please", "give", "me", "something", "more", "challenging"]]) == (53, 10, 2))
```

---------

Well done! We're almost done. We could use our two functions to compute the ARI for a given text as follows:


```python
sentences = [["this", "was", "rather", "easy"], 
             ["Please", "give", "me", "something", "more", "challenging"]]

n_chars, n_words, n_sents = extract_counts(sentences)
print(automatic_readability_index(n_chars, n_words, n_sents))
```

However, it would be nice to have a little more abstraction.

# Quiz!

Write the function `compute_ARI` that takes as argument a list of sentences (represented by lists of words) and returns the *Automatic Readability Index* for that input.


```python
def compute_ARI(sentences):
    # insert your code here
    
# do not modify the code below, it is for testing your answer only!
# it should output True if you did well
print(abs(compute_ARI(sentences) - 4.442) < 0.001)
```

--------------

Finally it would be nice to compare the readability of a number of texts. We need a function that iterates through the files in a directory and prints the Automatic Readability Index for each text. 

# Quiz!

Write a function `compute_ARIs` that takes the name of a directory as input and prints the Automatic Readbility Index for each document in that directory.


```python
def compute_ARIs(directory):
    # insert your code here
```

Remember that in Chapter 3, we plotted different basic statistics using Python plotting library matplotlib. Can you do the same for all ARIs?


```python
import matplotlib.pyplot as plt

# insert your code here
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

