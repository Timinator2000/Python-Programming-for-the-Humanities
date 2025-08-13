
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Quiz!

In the final quiz of this chapter we will ask you to write the frequency distribution over the words in data/austen-emma.txt to the file data/austen-frequency-distribution.txt. We will give you some code to get you started

```python runnable
# first open and read data/austen-emma.txt. Don't forget to close the infile
infile = open("data/austen-emma.txt")
text = # read the contents of the infile
# close the file handler
# clean the text

# next compute the frequency distribution using the function counter
frequency_distribution = 

# now open the file data/austen-frequency-distribution.txt for writing
outfile = 

for word, frequency in frequency_distribution.items():
    outfile.write(word + ";" + str(frequency) + '\n')
    
# close the outfile
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](CreativeCommons.png)
