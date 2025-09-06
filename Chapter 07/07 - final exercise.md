
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Final Exercise

Perhaps the biggest advantage of Object Oriented Programming is the ability to subclass objects. You could, for example, make a specialized IRSystem for searching through particular directories on your own laptop. In this final exercise you will implement a simple web searcher. This searcher can be initialized with a number of URLs of web pages. The searcher downloads these pages, strips all HTML markup and indexes the raw text. The searcher can then be used to query for particular web pages. 

Our implementation starts with a function to retrieve a webpage given a URL. The module [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) in Python's standard library, defines a number of functions and classes to open and read URLs. The function `urlopen` opens a `HTTPResponse` object, which has a method called `read`. Upon calling the `read` method, the complete webpage will be downloaded:


```python
import urllib.request

response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Albert_einstein")
response.read()[:1000]
```

The transcendent [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is a package to parse and create HTML (and a lot more). We will use this package to read the web pages:


```python
from bs4 import BeautifulSoup

response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Albert_einstein")
page = BeautifulSoup(response.read())
```

We call the method `get_text` on this web page to obtain a textual representation of the web page.


```python
text = page.get_text()
print(text[-1000:])
```

**a**) Implement the function `fetch_page`. It takes as input a URL and returns a textual representation of the corresponding web page.


```python
def fetch_page(url):
    # insert your code here
```

**b)** We implement the searcher as a subclass of the IRSystem:

    class WebSearcher(IRSystem):
    
Overwrite the method `index_collection`. The new method takes as input a list of URLs, fetches the textual contents for each of those URLs and adds the contents to the index.


```python
class WebSearcher(IRSystem):
    # insert your code here
```

Initialize your searcher and add a collection of web pages:


```python
searcher = WebSearcher()
searcher.index_collection(["https://en.wikipedia.org/wiki/Albert_einstein",
                           "http://nlp.stanford.edu/IR-book/",
                           "http://www.crummy.com/software/BeautifulSoup/"])
```

Finally search for documents in the index using different queries:


```python
searcher.present_results("soup")
```


```python
searcher.present_results("retrieval")
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

