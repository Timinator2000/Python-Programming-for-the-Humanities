
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Reading files

> __Playground note:__ In the original Jupyter Notebooks, the authors use `open` and `close` when working with files. Due to the environment in which this playground runs, the follow structure has been used instead:
>
> ```python
> with open('some_file.txt', 'r') as infile:
> ```
>
> As the authors mentioned in Chapter 1, indentation is very important in Python. `infile` will stay open as long as the following code is indented. Once the indentation ends, Python will automatically close `infile`. 

Say you have a text stored on your computer. How can we read that text using Python? Python provides a really simple function called `open` with which we can read texts. In the folder data you find a couple of small text excerpts that we will use in this chapter. Go ahead and have a look at them. We can open these files with the following command:

```python
with open('austen-emma-excerpt.txt') as infile:
```

We now print infile. What do you think that will happen?

```python runnable
with open('austen-emma-excerpt.txt') as infile:
    print(infile)
```

"Hey! That's not what I expected to happen!", you might think. Python is not printing the contents of the file but only some mysterious mention of some TextIOWrapper. This TextIOWrapper thing is Python's way of saying it has opened a connection to the file data/austen-emma-excerpt.txt. In order to read the contents of the file we must add the function read as follows:

print(infile.read())
read is a function that operates on TextWrapper objects and allows us to read the contents of a file into Python. Let's assign the contents of the file to the variable text:

infile = open('data/austen-emma-excerpt.txt')
text = infile.read()
The variable text now holds the contents of the file data/austen-emma-excerpt.txt and we can access and manipulate it just like any other string. After we read the contents of a file, the TextWrapper no longer needs to be open. In fact, it is good practice to close it as soon as you do not need it anymore. Now, lo and behold, we can achieve that with the following:

infile.close()
Quiz!
Just to recap some of the stuff we learnt in the previous chapter. Can you write code that defines the variable number_of_es and counts how many times the letter e occurs in text? (Tip: use a for loop and an if statement)

number_of_es = 0
# insert your code here

# The following test should print True if your code is correct 
print(number_of_es == 78)

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
