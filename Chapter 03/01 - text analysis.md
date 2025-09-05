
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Chapter 3: Text Analysis

In this chapter we will introduce you to the task of text analysis in Python. You will learn how to read an entire corpus into Python, clean it and how to perform certain data analyses on those texts. We will also briefly introduce you to using Python's plotting library *matplotlib*, with which you can visualize your data.

Before we delve into the main subject of this chapter, text analysis, we will first write a couple of utility functions that build upon the things you learnt in the previous chapter. Often we don't work with a single text file stored at our computer, but with multiple text files or entire corpora. We would like to have a way to load a corpus into Python.

Remember how to read files? Each time we had to open a file, read the contents and then close the file. Since this is a series of steps we will often need to do, we can write a single function that does all that for us. We write a small utility function `read_file(filename)` that reads the specified file and simply returns all contents as a single string.


```python
def read_file(filename):
    "Read the contents of FILENAME and return as a string."
    infile = open(filename) # windows users should use codecs.open after importing codecs
    contents = infile.read()
    infile.close()
    return contents
```

Now, instead of having to open a file, read the contents and close the file, we can just call the function `read_file` to do all that:


```python
text = read_file("data/austen-emma-excerpt.txt")
print(text)
```

In the directory `data/gutenberg/training` we have a corpus consisting of multiple files with the extension `.txt`. This corpus is a collection of English novels which we downloaded for you from the [Gutenberg](http://www.gutenberg.org) project. We want to iterate over all these files. You can do this using the `listdir` function from the `os` module. We import this function as follows:


```python
from os import listdir
```

After that, the `listdir` function is available to use. This function takes as argument the path to a directory and returns all the files and subdirectories present in that directory:


```python
listdir("data")
```

Notice that `listdir` returns a list and we can iterate over that list. Now, consider the following function:


```python
def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)
    return textfiles
```

The function `listdir` takes as argument the name of a directory and lists all filenames in that directory. We iterate over this list and append each filename that ends with the extension, `.txt` to a new list of `textfiles`. Using the `list_textfiles` function, the following code will read all text files in the directory `data/gutenberg/training` and outputs the length (in characters) of each:


```python
for filepath in list_textfiles("data/gutenberg/training"):
    text = read_file(filepath)
    print(filepath +  " has " + str(len(text)) + " characters.")
```


<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

