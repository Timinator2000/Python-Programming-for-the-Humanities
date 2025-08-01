
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Loops

Programming is most useful if we can perform a certain action on a range of different elements. For example, given a list of words, we would like to know the length of all words, not just one. Now you _could_ do this by going through all the indexes of a list of words and print the length of the words one at a time, taking up as many lines of code as you have indices. Needless to say, this is rather cumbersome.

Python provides the so-called `for`-statements that allow us to iterate through any iterable object and perform actions on its elements. The basic format of a `for`-statement is:

```text
for X in iterable:
```

That reads almost like English. We can print all letters of the word banana as follows:

for letter in "banana":
    print(letter)
The code in the loop is executed as many times as their are letters, with a different value for the variable letter at each iteration. Read the previous sentence again.

Likewise we can print all the items that are contained in a list:

colors = ["yellow", "red", "green", "blue", "purple"]
for whatever in colors:
    print("This is color " + whatever)
Since dictionaries are iterable objects as well, we can iterate through our good reads collection as well. This will iterate over the keys of a dictionary:

for book in good_reads:
    print(book)
We can also iterate over both the keys and the values of a dictionary, this is done as follows:

good_reads.items()
for x, y in good_reads.items():
    print(x + " has score " + str(y))
Using items() will, at each iteration, return a nice pair of the key and the value. In the example above the variable book will loop over the keys of the dictionary, and the variable score loops over the respective values.

The above way is the most elegant way of looping over dictionaries, but try to see if you understand the following alternative as well:

for book in good_reads:
    print(book, "has score", good_reads[book])
Quiz!
The function len() returns the length of an iterable item:

len("banana")
We can use this function to print the length of each word in the color list. Write your code in the box below:

colors = ["yellow", "red", "green", "blue", "purple"]
# insert your code here
Now write a small program that iterates through the list colors and appends all colors that contain the letter r to the list colors_with_r. (Tip: use colors_with_r.append)

colors = ["yellow", "red", "green", "blue", "purple"]
colors_with_r = []
# insert you code here
What we have learnt
Here is an overview of the new concepts, statements and functions we have learnt in this section. Again, go through the list and make sure you understand them all.

loop
for statement
iterable objects
variable assignment in a for loop
<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
