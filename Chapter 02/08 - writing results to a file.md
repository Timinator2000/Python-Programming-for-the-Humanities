
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Writing results to a file

We have accomplished a lot! You have learnt how to read files using Python from your computer, how to manipulate them, clean them up and compute a frequency distribution of the words in a text file. We will finish this chapter with explaining to you how to write your results to a file. We have already seen how to read a text from our disk. Writing to our disk is only slightly different. The following lines of code write a single sentence to the file `first-output.txt`.

```python
with open("first-output.txt", mode="w") as f:
    f.write("My first output.")
```

Go ahead and open the file `first-output.txt` located in the folder where this course resides. As you can see it contains the line `My first output.`. To write something to a file we open, just as in the case of reading a file, a `TextIOWrapper` which can be seen as a connection to the file first-output.txt. The difference with opening a file for reading is the _mode_ with which we open the connection. Here the mode says `w`, meaning "open the file for writing". To open a file for reading, we set the mode to `r`. However, since this is Python's default setting, we may omit it.

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)
