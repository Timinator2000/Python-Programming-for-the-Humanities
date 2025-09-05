
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Authorship Attribution 

In this section you will implement the core of an authorship attribution application. You won't build a full stand-alone application, but rather focus on the core functions for classifying new texts for their authors.

The core of our application will be a naive bayes classifier. Following good programming principles, we will try to make this classifier as generic as possible. This allows us to use the classifier in other contexts than authorship attribution, such as text classification and classification in general.

The naive bayes classifier is a probabilistic classifier that, given a set of features, tries to find the class with the highest probability. It is based on applying Bayes' theorem and is called naive because of its strong independence assumption between features. This means that the absence or presence of each feature is assumed to be independent of each other. We compute the posterior probability of a class as the joint probability of all features given that class:

<BR>

```math
P(y|x_1,\ldots,x_n) \propto P(y) \prod^n_{i=1} P(x_i|y)
```

<BR>

Classification is based on the *maximum a posteriori* or MAP descision rule which simply picks the class (or author in our case) that is most probable:

<BR>

```math
classify(x_1, \ldots, x_n) = \arg\max_y P(y) \prod^n_{i=1} P(x_i|y)
```

<BR>

The main function we will implement has a simple job: take a text as an argument and classify it as being written by one of the authors. Let's again apply some wishful thinking and implement the function as follows:


```python
def predict_author(text, feature_database):
    "Predict who wrote this text."
    return classify(score(extract_features(text), feature_database))
```

This function takes two arguments: the text to classify and the training data against which we want to classify the text. The function is basically an abstraction layer on top of `classify`,  `extract_features` and `score`. `classify` is a simple function that takes a dictionary of {$author_i$:  $P(author_i|text)$} and returns the author that is most probable. Let's implement this function.

# Quiz!

Implement the function `classify`. It takes one argument, `scores` which is a dictionary with authors as keys and the probability of an author as value. Return the author with maximum probability. (Tip: use the built in function `max`, see [the documentation](http://docs.python.org/3/library/functions.html#max))


```python
scores = {"Hermans": 0.15, "Voskuil": 0.55, "Reve": 0.2, "Mulisch": 0.18, "Claus": 0.02}

def classify(scores):
    # insert your code here
    
print(classify(scores) == "Voskuil")
```

---------

The function `extract_features` is rather straightforward as well. We'll build this function on top of the functions we defined in the previous chapters. For the moment we will assume that our model is a bag-of-words (BOW) model where the only features are individual words. We will define `extract_features` as an abstraction layer on top of `read_corpus_file` and `tokenise` as follows:


```python
from pyhum.preprocessing import read_corpus_file, tokenize

def extract_features(filename):
    return tokenise(read_corpus_file(filename))
```

Now for our training data, we need to store for each word how often it occurs with a particular author. As our data structure we will use a nested dictionary of the following structure `author -> word -> count`. We'll store the counts in the variable `feature_database`.

(For more information about `defaultdict`, see [the defaultdict documentation](http://docs.python.org/3/library/collections.html#collections.defaultdict).  For more information about `lambda` expressions, see [the lambda documentation](http://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions).)


```python
from collections import defaultdict

feature_database = defaultdict(lambda: defaultdict(int))
```

--------

To fill our `feature_database` we will need a couple of functions. First we need a function that returns the author of a particular text. To make things a little easier, we named our training files with the author's name followed by the title of the book, i.e. `austen-emma.txt`. Or when the path is part of the filename, `/path/to/austen-emma.txt`.

# Quiz!

Write a function `extract_author` that takes a filename as input and returns the name of the author.


```python
def extract_author(filename):
    # insert your code here

# do not modify the code below, it is for testing your answer only!
# it should output True if you did well
print(extract_author("Austen-emma.txt") == "Austen")
print(extract_author("/path/to/Austen-emma.txt") == "Austen")
```

Next we'll need a function, `update_counts`, that takes as argument the name of an author and the words extracted using `extract_features` and adds these to our `feature_database`. The function should return a new updated version of the `feature_database`.


```python
from preprocess import tokenise

def update_counts(author, text, feature_database):
    # insert your code here
    return feature_database

# do not modify the code below, for testing only!
feature_database = defaultdict(lambda: defaultdict(int))
feature_database = update_counts("Anonymous", "This was written with a lack of inspiration", 
                                 feature_database)
test_database = defaultdict(lambda: defaultdict(int))
for word in "This was written with a lack of inspiration".split():
    test_database["Anonymous"][word] += 1
print(sorted(feature_database.items()) == sorted(test_database.items()))
```

-------

Finally we define a function `add_file_to_database` that takes a filename and the `feature_database` as input, extracts the author from the filename and adds the feature counts to the `feature_database`. We define it as follows:


```
def add_file_to_database(filename, feature_database):
    return update_counts(extract_author(filename), 
                         extract_features(filename), 
                         feature_database)
```

# Quiz!

Now that we have a function to add one file to the `feature_database`, we need a function that adds an entire corpus to the database. Write a function that takes the name of a directory as input and add all files in this directory to the `feature_database`. Again, the function should return an updated version of our database.


```python
import os

def add_directory_to_database(directory, feature_database):
    # insert your code here
    return feature_database
```

---------

We now have a function to extract the features of a document. We have also defined a couple of functions to add those features to our `feature_database`. It is now time to implement the core function of our authorship attribution application. 

Before we will implement the `score` function we will first implement a function to compute the probability of one feature given an author. There are two things to note with regard to this function.

First, if a given author and a word never occur together in the `feature_database`, the probabilty of that class will be zero (think about this, if you don't understand why). Needless to say this is rather problematic. A common strategy to surpass this problem is to add pseudocounts to the observed counts, normally 1. The pseudocounts need to be incorporated in both the numerator and the denominator.

Second, the probability of one feature will normally be quite small. If we now multiply all probabilities of our features given an author we will get a very small number, possibly too small, to be adequately represented by Python. Consider the code below:


```python
x = 0.00000000000000001
for i in range(30):
    x = x * 0.000000000000001
    print(x)
```

After less than 30 multiplications, the values are too small for Python to distinguish them from each other. Even worse, the values default to zero and as we know multiplying by zero will return zero, and therefore all our probabilities could be zero! We therefore take the log of the individual feature probabilities and sum them to obtain our final score. Let's implement the `log_probability` function first.


```python
from math import log

def log_probability(feature_counts, features_sum, n_features):
    return log((feature_counts + 1.0) / (features_sum + n_features))
```

`feature_counts` is the number of times the given feature occurs with a particular author. `features_sum` is the sum of all feature counts for that author. `n_features` is the number of unique features in our `feature_database` (needed for pseudocounts). Now that we have defined this crucial function, we are ready to implement our `score` function.

# Quiz!

The function `score` takes as input a list of features and the `feature_database`. It should return a dictionary with authors as keys and their probabilities given the list of features as values. We'll provide the basic frame for this function below and ask you to fill in the details. This is without doubt the most challenging Quiz! you have seen so far and we will be very impressed if you get it right. 


```python
def score(features, feature_database):
    "Predict who wrote the document on the basis of the corpus."
    scores = defaultdict(float)
    # compute the number of features in the feature database here
    for author in feature_database:
        # compute the probability of features given that author here
    return scores

# do not modify the code below, for testing your answer only! 
# It should return True if you did well!
features = ["the", "a", "the", "be", "book"]
feature_database = defaultdict(lambda: defaultdict(int))
feature_database["A"]["the"] = 2
feature_database["A"]["a"] = 5
feature_database["A"]["book"]= 1
feature_database["B"]["the"] = 5
feature_database["B"]["a"] = 1
feature_database["B"]["book"] = 6
print(abs(dict(score(features, feature_database))["A"] - -7.30734) < 0.001)
```

---------

Wow! You have really done a great job. You have implemented almost entirely by yourself a complete naive bayes classifier that can be used for all kinds of classification problems, such as document classification and authorship attribution. 

Now we should put all things together and test how well our system works. In the folder `data/gutenberg/training` we have provided a couple of training documents from different author. The folder `data/gutenberg/testing` provides three test documents. Let's test our classifier on one of those documents!


```python
# first define the feature_database
feature_database = defaultdict(lambda: defaultdict(int))
feature_database = add_directory_to_database("data/gutenberg/training", feature_database)
print(predict_author("data/gutenberg/testing/milton-poetical.txt", feature_database))
```

It would be nice to evaluate our classifier on more than one document and to obtain some sort of score of how well our classifier performs. We will implement two functions: `test_from_corpus` and `analyze_results`. 

# Quiz!

`test_from_corpus` takes as input the name of a directory and a trained feature database. It then tries to predict the author of all files in the given directory. The function should return a list of `(ground-truth-author, predicted-author)` tuples.


```python
def test_from_corpus(directory, feature_database):
    results = []
    # insert your code here
    return results
```

---------

Finally we will implement the function `analyze_results` which takes a list of `(ground-truth-author, predicted-author)` tuples as input and returns the accuracy of the classifier, which is defined as:

<BR>

```math
accuracy(X) = \frac{\textrm{number of correct predictions}}{\textrm{total number of predictions}}
```

# Quiz!

Implement the function `analyze_results` and test your classifier on the test corpus in `data/gutenberg/testing`:

```python
def analyze_results(results):
    # insert your code here

# do not modify the code below, for testing only!
print(analyze_results([("A", "A"), ("A", "B"), ("C", "C"), ("D", "C"), ("E", "E")]) == 0.6)
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

