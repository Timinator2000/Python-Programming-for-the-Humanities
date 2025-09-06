
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Query the Index

Now that we have an efficient, sparse data structure to represent our collection, how can we use that stucture to efficiently process user queries? Our index is represented as a Python dictionary which allows us to query the index for single terms, using

    s = IRSystem()
    s.tdf[term]

which will return a set of all documents in which that term occurs. But how do we search for documents that contain two or more terms? Python's data structure `set` defines a convenient method called `intersection` with which we can extract all items common to two or more sets:

```python
a = {'a', 'b', 'c', 'd'}
b = {'c', 'a', 'e', 'f'}
print(a.intersection(b))
```

We can make use of this method to implement the method `query` which takes as argument an arbitrary number of query terms and returns all documents in which those terms occur.

# Quiz!

Implement the method `IRSystem.query(*terms)`. The method should return an iterable containing all ID's of the documents in which all query terms occur.

```python
class IRSystem:
    """A very simple Information Retrieval System. The constructor 
    s = IRSystem() builds an empty system. Next, index several documents 
    with s.index_document(ID, text). Then ask queries with 
    s.query('term1', 'term2') to retrieve the matching documents."""
    
    def __init__(self):
        "Initialize an IR Sytem."
        self.tdf = defaultdict(set)
        self.doc_ids = []
                
    def index_document(self, doc_id, words):
        "Add a new unindexed document to the system."
        self.doc_ids.append(doc_id)
        for word in words:
            self.tdf[word].add(doc_id)

    def index_collection(self, filenames):
        "Index a collection of documents."
        for filename in filenames:
            self.index_document(os.path.basename(filename), 
                                tokenize(open(filename).read()))
            
    def query(self, *terms):
        "Query the system for documents in which all terms occur."
        # insert your code here
    
# these tests should return True if your code is correct
s = IRSystem()
s.index_collection(glob.glob('data/haggard/*.txt'))

print('Beatrice 3096.txt' in s.query("master", "children"))
print('Fair Margaret 9780.txt' in s.query("eye", "father", "work"))
```

---

Our Information Retrieval system starts to look quite good. We have written functions to tokenize documents, index documents and query the index for documents. In the query method above, we made the simplifying assumption that as long as two documents contain a particular search term, they are equally relevant. However, our intuition says that documents that contain more instances of a particular term are more relevant than documents with less instances. To account for this intuition we need a way to score and sort our search results.

Let's start with a very naive and simple scoring function: document frequency. This scoring function simply sums the document frequencies of each search term in a particular document:

```math
\textrm{score}(q_1, q_2, \ldots, q_n) = \sum^n_{i=1} df(q_i)
```

where $n$ is the number of search terms and $df$ the document frequency of term $q_i$ in a document.

To compute this formula we need to obtain the frequency of each word in each document. The method `index_document` seems an appropriate place to extract these frequencies. For each term we store how often that term occurs in each document. Note that in the previous implementation of `index_document`, the variable `tdf` is represented by a dictionary with sets of document ID's as values. We will change this data structure to a structure that allows us to store the document frequencies:


```python
from collections import Counter

class IRSystem:
    """A very simple Information Retrieval System. The constructor 
    s = IRSystem() builds an empty system. Next, index several documents 
    with s.index_document(ID, text). Then ask queries with 
    s.query('term1', 'term2') to retrieve the matching documents."""
    
    def __init__(self):
        "Initialize an IR Sytem."
        self.tdf = defaultdict(Counter) # changed!
        self.doc_ids = []
                
    def index_document(self, doc_id, words):
        "Add a new unindexed document to the system."
        self.doc_ids.append(doc_id)
        for word in words:
            self.tdf[word][doc_id] += 1 # changed!

    def index_collection(self, filenames):
        "Index a collection of documents."
        for filename in filenames:
            self.index_document(os.path.basename(filename), 
                                tokenize(open(filename).read()))            
            
    def query(self, *terms):
        "Query the system for documents in which all terms occur."
        return set.intersection(*map(self.tdf.get, terms))
```

I represent the `tdf` variable as a dictionary with [Counter](https://docs.python.org/dev/library/collections.html#collections.Counter) objects as default values. The `Counter` object is a very convenient structure for counting hashable objects. As you can see, we only had to adjust two lines in our original system. Before we continue, make sure you understand what is happening here. We reinitialize our IR system:


```python
s = IRSystem()
s.index_collection(glob.glob('data/haggard/*.txt'))
```

Let's inspect the term-document frequency matrix:


```python
s.tdf['master'].most_common(n=10)
```

The class `Counter` has a method called `most_common`. It returns the $n$ most common items in a `Counter` object. We have a data structure that stores the information about the frequency of words in documents. The next step will be to to adapt our query function in such a way that it returns a ranked list of documents where each document is sorted on the basis of the equation above.

# Quiz!

1. The method `query` in the class definition below calls the method `score`. This method takes as arguments a document ID and an arbitrary number of terms. It returns the sum of the frequencies of these terms in this document. Implement the method `score`.


```python
class IRSystem:
    """A very simple Information Retrieval System. The constructor 
    s = IRSystem() builds an empty system. Next, index several 
    documents with s.index_document(ID, text). Then ask queries 
    with s.query('term1', 'term2') to retrieve the top n matching 
    documents."""
    
    def __init__(self):
        "Initialize an IR Sytem."
        self.tdf = defaultdict(Counter)
        self.doc_ids = []
                
    def index_document(self, doc_id, words):
        "Add a new unindexed document to the system."
        self.doc_ids.append(doc_id)
        for word in words:
            self.tdf[word][doc_id] += 1

    def index_collection(self, filenames):
        "Index a collection of documents."
        for filename in filenames:
            self.index_document(os.path.basename(filename), 
                                tokenize(open(filename).read()))
                
    def score(self, doc_id, *terms):
        "Score a document for a particular query using the sum of the term frequencies."
        # insert your code here
            
    def query(self, *terms, n=10):
        """Query the system for documents in which all terms occur. Returns
        the top n matching documents."""
        scores = {doc_id: self.score(doc_id, *terms) for doc_id in self.doc_ids}
        return sorted(scores, key=scores.get, reverse=True)[:n]


# these tests should return True if your code is correct
s = IRSystem()
s.index_collection(glob.glob('data/haggard/*.txt'))

print(s.query("master")[0] == 'The Ancient Allan 5746.txt')
print(s.query("egg", "shell")[0] == 'Dawn 10892.txt')
```

2. Give at least two reasons why this way of scoring and sorting our documents is probably not such a good idea, after all.

    * Double click this cell and write down your answer.*

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

