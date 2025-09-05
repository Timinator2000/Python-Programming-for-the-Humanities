
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Exploratory data analysis

As a first exploratory data analysis, we are going to compute for each night how many sentences it contains and how many words. It is quite easy to count the number of sentences per night, since each night is represented by a list of sentences.


```python
sentences_per_night = []
for night in corpus:
    sentences_per_night.append(len(night))
print(sentences_per_night[:10])
```

Using the function `max` we can find out what the highest number of sentences is:


```python
max(sentences_per_night)
```

Similarly, if we would like to now what the lowest number of sentences is, we use the function `min`:


```python
min(sentences_per_night)
```

# Quiz!

The function `sum` takes a list of numbers as input and returns the sum:


```python
print(sum([1, 3, 3, 4]))
```

Use this function to compute the average number of sentences per night. Note if you use Python 2.7, you will need to convert the result of sum, which will be an integer to a `float`, using `float(some_number)`. 


```python
# if you use Python 3.x, both print statements will return 
# the same thing and you don't need to worry.
number = 1
print(number)
number = float(number)
print(number)
```


```python
# insert your code here
```

---

Given our data structure of a list of sentences which are themselves lists of words, it is a little trickier to count for each night how many words it contains. One possible way is the following:


```python
words_per_night = []
for night in corpus:
    n_words = 0
    for sentence in night:
        n_words += len(sentence)
    words_per_night.append(n_words)
```

Make sure you really understand these lines of code as you will need them in the next quiz. 

The suspense created by Shahrazad’s story-telling skills is intriguing, especially the “cliff-hanger” ending each night which she uses to avert her own execution (and possibly that of womanhood). Every night she tells the Sultan a story only to stop at dawn and she picks up the thread the next night. But does it really take the whole night to tell a particular story?

I am not aware of any exact numbers about how many words people speak per minute. Averages seem to fluctuate between 100 and 200 words per minute. Narrators are advised to use approximately 150 words per minute in audiobooks. I suspect that this number is a little lower for live storytelling and assume it lies around 130 words per minute (including pauses). Using this information, we can compute the time it takes to tell a particular story as follows:

<BR>

![Story Time](StoryTimeFormula.png)

<BR>

# Quiz!

1. Write a function called `story_time` that takes as input a text. Given a speed of 130 words per minute, compute how long it takes to tell that text.


    ```python
    def story_time(text):
        # insert your code here

    # these tests should return True if your code is correct
    print(story_time([["story", "story"]]) * 130 == 2.0)
    ```

2. Compute the story_time for each night in our corpus. Assign the result to the variable `story_time_per_night`.


    ```python
    story_time_per_night = []
    # insert your code here
    print(story_time_per_night[:10])
    ```

3. Compute the average, minimum and maximum story telling time.


    ```python
    # insert your code here
    ```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

