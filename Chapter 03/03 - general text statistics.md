
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

## General Text Statistics

> When the next night came, Dinarazad said to her sister Shahrazad: ‘In God’s name, sister, if you are not asleep, then tell us one of your stories!’ Shahrazad answered: ‘With great pleasure! I have heard tell, honoured King, that…’

*Alf Laylah Wa Laylah*, *the Stories of One Thousand and One Nights* is a collection of folk tales, collected over many centuries by various authors, translators, and scholars across West, Central and South Asia and North Africa, forms a huge narrative wheel with an overarching plot, created by the frame story of Shahrazad.

The stories begin with the tale of king Shahryar and his brother, who, having both been deceived by their respective Sultanas, leave their kingdom, only to return when they have found someone who — in their view — was wronged even more. On their journey the two brothers encounter a huge jinn who carries a glass box containing a beautiful young woman. The two brothers hide as quickly as they can in a tree. The jinn lays his head on the girl’s lap and as soon as he is asleep, the girl demands the two kings to make love to her or else she will wake her ‘husband’. They reluctantly give in and the brothers soon discover that the girl has already betrayed the jinn ninety-eight times before. This exemplar of lust and treachery strengthens the Sultan’s opinion that all women are wicked and not to be trusted. 

When king Shahryar returns home, his wrath against women has grown to an unprecedented level. To temper his anger, each night the king sleeps with a virgin only to execute her the next morning. In order to make an end to this cruelty and save womanhood from a "virgin scarcity", Sharazad offers herself as the next king’s bride. On the first night, Sharazad begins to tell the king a story, but she does not end it. The king’s curiosity to know how the story ends, prevents him from executing Shahrazad. The next night Shahrazad finishes her story, and begins a new one. The king, eager to know the ending of this tale as well, postpones her execution once more. Using this strategy for One Thousand and One Nights in a labyrinth of stories-within-stories-within-stories, Shahrazad attempts to gradually move the king’s cynical stance against women towards a politics of love and justice (see Marina Warner’s *Stranger Magic* (2013) in case you're interested).

The first European version of the Nights was translated into French by Antoine Galland. Many translations (in different languages) followed, such as the (heavily criticized) English translation by Sir Richard Francis Burton entitled *The Book of the Thousand and a Night* (1885). This version is freely available from the Gutenberg project (see [here](http://www.gutenberg.org)), and will be the one we will explore here.

# Quiz!

In the directory `data/arabian_nights` you will find 999 files. This is because in Burton's translation some nights are missing. The name of the file represents the corresponding night of storytelling in *Alf Laylah Wa Laylah*. Go have a look. Use the tokenize function and the corpus reading function we have defined above and tokenize and clean each night. Store the result in the variable named `corpus`.


```python
# insert your code here
```

---

Great job! You now should have a corpus containing 999 texts. It is always important to check whether our code actually produces the desired results. Let's check whether we indeed have 999 texts:


```python
print(len(corpus))
```

OK, that seems to be correct. It would be convenient for further processing to have the corpus in chronological order. Let's have a look the first 20 files returned by `list_textfiles`:


```python
list_textfiles("data/arabian_nights")[:20]
```

As you can see the files are sorted by their string name and not by their numbering. To be able to sort the files by their numbers we must first remove the extension `.txt` as well as the directory `data/arabian_nights/`.

---

# Quiz!

1. Write a function `remove_txt` that takes as argument a string and some extension that you want to remove. It should return the string without the extension. Tip: use the function `splitext` from the `os.path` module. Look up the documentation [here](http://docs.python.org/3.4/library/os.path.html#os.path.splitext).


    ```python
    from os.path import splitext

    def remove_ext(filename):
        # insert your code here
        
    # these tests should return True if your code is correct
    print(remove_ext("data/arabian_nights/1.txt") == "data/arabian_nights/1")
    print(remove_ext("ridiculous_selfie.jpg") == "ridiculous_selfie")
    ```

2. Write a function `remove_dir` that takes as argument a filepath and removes the directory from a filepath. Tip: use the function `basename` from the `os.path` module. Look up the document [here](http://docs.python.org/3.4/library/os.path.html#os.path.basename)


    ```python
    from os.path import basename

    def remove_dir(filepath):
        # insert your code here
        
    # these tests should return True if your code is correct
    print(remove_dir("data/arabian_nights/1.txt") == "1.txt")
    print(remove_dir("/a/kind/of/funny/filepath/to/file.txt") == "file.txt")
    ```

3. Combine the two functions `remove_ext` and `remove_dir` into one function `get_filename`. This function takes as argument a filepath and returns the name (without the extensions) of the file.


    ```python
    def get_filename(filepath):
        # insert your code here
        
    # these tests should return True if your code is correct
    print(get_filename("data/arabian_nights/1.txt") == '1')
    ```

---

The final step is to convert numbers represented as string (e.g. "1" and "10") to a number. This can be achieved by using the function `int`:


```python
x_as_string = "1"
x_as_int = int(x_as_string)
print(x_as_int)
```

The process of converting a string into an integer, is called *type casting*. Strings are different types than integers. To see this, have a look at the following:


```python
x = "1"
y = "2"
print(x + y)
```

12? Yes, 12. This is because, as you might remember from the first chapter, we can use the `+` operator to concatenate two strings. If we apply the same operation to integers, as in:


```python
x = 1
y = 2
print(x + y)
```

we get the expected result of 3.

# Quiz!

Combine the functions `int` and `get_filename` into the function `get_night` to obtain the integer corresponding to a night.


```python
def get_night(filepath):
    # insert your code here

# these tests should return True if your code is correct
print(get_night("data/arabian_nights/1.txt") == 1)
```

---

OK, so now we can convert the filepaths to integers corresponding to the nights of storytelling. But how will we use that to sort the corpus in chronological order? In chapter 1 we briefly discussed how to sort your collection of good reads. In combination with our `get_night` function, we can use `sort` to obtain a nicely chronologically ordered list of stories. Prepare yourself for some real Python magic, because the following lines of code might be a little dazzling...

First we list all files using `list_textfiles` and store it in the variable `filenames`:


```python
filenames = list_textfiles('data/arabian_nights')
```

Next we call the function `.sort()` on this list and supply as keyword our function `get_night`:


```python
filenames.sort(key=get_night)
filenames[:20]
```

As you can see, we now have a perfectly chronologically ordered list of filenames. But how, **HOW!** did that work? As you might have guessed, the argument of `sort`: `key=get_night`, has something to do with all this magic. Without this argument, Python would just sort the filenames alphabeticaly:


```python
filenames = list_textfiles('data/arabian_nights')
filenames.sort()
print(filenames[:20])
```

However, if we supply a function to `key`, Python will internally first apply that function to all items we want to sort. In our case this means Python converts all filepaths to integers. After that Python sorts the list. Then for each converted item it returns the corresponding item in the original list. (Technically this is not an accurate description, but it basically comes down to this.)

If you still feel a little dizzy after all this, don't be afraid. Sometimes it is good enough to use a particular piece of code even if you don't completely understand it. We can now use these functions to reload the corpus, this time in chronological order:


```python
corpus = []
filenames = list_textfiles("data/arabian_nights")
filenames.sort(key=get_night)
for filename in filenames:
    text = read_file(filename)
    corpus.append(tokenize(text))
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

