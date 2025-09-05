
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Visualizing general statistics

Now that we have computed a range of general statistics for our corpus, it would be nice to visualize them. Python's plotting library *matplotlib* (see [here](http://matplotlib.org)) allows us to produce all kinds of graphs. We could for example, plot for each story, how many sentences it contains:


```python
import matplotlib.pyplot as plt

plt.plot(sentences_per_night)
```

# Quiz!

1. Can you do the same for `words_per_night`?


    ```python
    # insert your code here
    ```

2. And can you do the same for `story_time_per_night`?


    ```python
    # insert your code here
    ```

3. In this final exercise we will put everything together what we have learnt so far. We want you to write a function `positions_of` that returns for a given word all sentence positions in the *Arabian Nights* where that word occurs. We are not interested in the positions relative to a particular night, but only to the corpus as a whole. Use that function to find all occurences of the name Sharahzad and store the corresponding indexes in the variable `positions_of_shahrazad`. Do the same thing for the name *Ali*. Store the result in `positions_of_ali`. Finally, find all occurences of *Egypt* and store the indexes in `positions_of_egypt`. Tip: (1) remember that we lowercased the entire corpus! (2) remember that indexes start at 0.


    ```python
    def positions_of(word):
        #insert your code here

    positions_of_shahrazad = positions_of("shahrazad")
    positions_of_ali = positions_of("ali")
    positions_of_egypt = positions_of("egypt")
    ```

If everything went well, the following lines of code should produce a nice dispersion plot of all sentence occurences of Shahrazad, Ali and Egypt in the corpus.


```python
plt.figure(figsize=(20, 8))
names = ["Shahrazad", "Ali", "Egypt"]
plt.plot(positions_of_shahrazad, [1]*len(positions_of_shahrazad), "|", markersize=100)
plt.plot(positions_of_ali, [2]*len(positions_of_ali), "|", markersize=100)
plt.plot(positions_of_egypt, [0]*len(positions_of_egypt), "|", markersize=100)
plt.yticks(range(len(names)), names)
_ = plt.ylim(-1, 3)
```

---

> Then Shahrazad reached the morning, and fell silent in the telling of her tale…

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

