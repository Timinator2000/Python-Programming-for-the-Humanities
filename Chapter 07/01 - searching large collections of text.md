
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Chapter 7 - Searching large Collections of Text

Imagine you have collected a large number of documents for your research. A large collection of English novels from [Project Gutenberg](http://www.gutenberg.org/), for example, or all volumes of the *New York Times* from 1987 until 2007 (see [here](https://catalog.ldc.upenn.edu/LDC2008T19)). The *New York Times* corpus contains over 1.8 million articles. If on average each article consists of only 500 words (the actual number will probably be higher), the complete corpus will contain about 900 million words. How can we search through such large collections of text? How can we efficiently find the information we are looking for? 

These questions are central to the current chapter. We will discuss important concepts from *Information Retrieval* to index and search collections (of text), such as the *inverted index* and the ranking metric *Okapi BM25*. This wouldn't be a Python course if you didn't have to implement all discussed techniques and methods. We will implement an important search algorithm which allows you to efficiently and reliably extract information from corpora. Along the way we will discuss quite some new and important programming techniques and constructs. We will also further our knowledge about the framework of Object Oriented Programming or OOP. We have quite some ground to cover, so let's get started.

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

