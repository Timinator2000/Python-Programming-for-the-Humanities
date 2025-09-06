
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Okapi BM25

Our scoring method contains multiple flaws. Most worrying is that it does not control for the lengths of our documents. Needless to say, this greatly influences our final lists. We need to think harder about what makes it that a search term is more or less relevant for a particular document.

The frequency with which terms occur in a document functions as an important cue to the importance of a document. The document is even more important when it contains many examples of this search term while the term occurs only in a limited number of other documents. In Information Retrieval a ranking metric that attempts to capture this intuition is [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25). The metric has proven to be one of the most successful ranking functions. In one of its many versions it is computed as follows:

```math
score(q_1, q_2, \ldots, q_n) = \sum^n_{i=1} IDF(q_i) \cdot \frac{df(q_i, D) \cdot (k_1 + 1)}{df(q_i, D) + k_1 \cdot (1 - b + b \cdot \frac{|D|}{\textrm{avgdl}})}
```

where $Q$ represents a query and $df(q_i, D)$ is the frequency of the i'th term in $Q$ in document $D$. $|D|$ is the length of document $D$ in number of word tokens and avgdl is the average document length. The parameters $b$ and $k_1$ are commonly set to $0.75$ and $1.2$, respectively. We compute the I(nverse) D(ocument) F(requency) weight using:

```math
IDF(q_i) = \log \frac{N - n(q_i) + 0.5}{n(q_i) + 0.5}
```

where $N$ is the number of documents in the corpus and $n(q_i)$ the number of documents that contain $q_i$.

We will implement this formula in our `score` method. Before we do that, we will first make a list of all the information we need to compute the formula:

1. the frequency of a term $q_i$ in document $D$;
2. the length of document $D$;
3. the average length of all documents in the collection;
4. the IDF weight of a term $q_i$.

Our current implementation already stores the document frequency of each term in each document (1). Thus, we only need to write code to extract the last three items: (2) the length of each document, (3) the average document length and (4) the IDF weight of each unique term.

# Quiz!

1. In this exercise you have to add the length of each document in our collection to the IR system. Reimplement the `index_document` method. Besides updating the term-document frequencies of each term, it should update the `Counter` object `lengths` in such a way that for each document ID it stores the length of the document being indexed.


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
            self.lengths = Counter()
            self.doc_ids = []
                    
        def index_document(self, doc_id, words):
            "Add a new unindexed document to the system."
            self.doc_ids.append(doc_id)
            # insert your code here

        def index_collection(self, filenames):
            "Index a collection of documents."
            for filename in filenames:
                self.index_document(os.path.basename(filename), 
                                    tokenize(open(filename).read()))
                
        def score(self, doc_id, *terms):
            "Score a document for a particular query using the sum of the term frequencies."
            return sum(self.tdf[term][doc_id] for term in terms)
                
        def query(self, *terms, n=10):
            """Query the system for documents in which all terms occur. Returns
            the top n matching documents."""
            scores = {doc_id: self.score(doc_id, *terms) for doc_id in self.doc_ids}
            return sorted(scores, key=scores.get, reverse=True)[:n]


    # these tests should return True if your code is correct
    s = IRSystem()
    s.index_collection(glob.glob('data/haggard/*.txt'))

    print(s.lengths['Dawn 10892.txt'] == 192299)
    ```

2. Once we have obtained the document length for each document, computing the average document length is trivial. In this exercise we will focus on the IDF weights. To compute the IDF weight for a particular term $q_i$ we need to know two things:

    * how many documents $N$ there are in our collection;
    * in how many documents that term occurs: $n(q_i)$.

We will implement a helper method called `_document_frequency`. It should return a dictionary in which we store for each term the number of documents in which that term occurs. You will also need to adapt the `index_document` method in such a way that the variable `N` represents the number of documents that have been indexed.

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
        self.lengths = Counter()
        self.doc_ids = []
        self.N = 0
                
    def index_document(self, doc_id, words):
        "Add a new unindexed document to the system."
        self.doc_ids.append(doc_id)
        # insert you code here
    
    def index_collection(self, filenames):
        "Index a collection of documents."
        for filename in filenames:
            self.index_document(os.path.basename(filename), 
                                tokenize(open(filename).read()))

    def _document_frequency(self):
        "Return the document frequency for each term in self.tdf."
        # insert your code here
    
    def score(self, doc_id, *terms):
        "Score a document for a particular query using the sum of the term frequencies."
        return sum(self.tdf[term][doc_id] for term in terms)
            
    def query(self, *terms, n=10):
        """Query the system for documents in which all terms occur. Returns
        the top n matching documents."""
        scores = {doc_id: self.score(doc_id, *terms) for doc_id in self.doc_ids}
        return sorted(scores, key=scores.get, reverse=True)[:n]


# these tests should return True if your code is correct
s = IRSystem()
s.index_collection(glob.glob('data/haggard/*.txt'))

print(s._document_frequency()['children'] == 59)
```

---

We now have all the ingredients to compute the Okapi BM25 score. Lets put everything together and implement a complete version of our IR system:


```python
import glob, os
from math import log

class IRSystem:
    """A very simple Information Retrieval System. The constructor 
    s = IRSystem() builds an empty system. Next, index several documents 
    with s.index_document(text, url). Then ask queries with 
    s.query('term1', 'term2', n=10) to retrieve the top n 
    matching documents."""
    
    def __init__(self, b=0.75, k1=1.2):
        "Initialize an IR Sytem."
        self.N = 0
        self.lengths = Counter()
        self.tdf = defaultdict(Counter)
        self.doc_ids = []
        self.b = b
        self.k1 = k1
        self._all_set = False
        
    def __repr__(self):
        return '<IRSystem(b={self.b}, k1={self.k1}, N={self.N})>'.format(self=self)
        
    def index_document(self, doc_id, words):
        "Add a new unindexed document to the system."
        self.N += 1
        self.doc_ids.append(doc_id)
        for word in words:
            self.tdf[word][doc_id] += 1
            self.lengths[doc_id] += 1
        self._all_set = False
        
    def index_collection(self, filenames):
        "Index a collection of documents."
        for filename in filenames:
            self.index_document(os.path.basename(filename), 
                                tokenize(open(filename).read()))
    
    def _document_frequency(self):
        "Return the document frequency for each term in self.tdf."
        return {term: len(documents) for term, documents in self.tdf.items()}
    
    def score(self, doc_id, *query):
        "Score a document for a particular query using Okapi BM25."
        score = 0
        length = self.lengths[doc_id]
        for term in query:
            tf = self.tdf[term][doc_id]
            df = self.df.get(term, 0)
            idf = log((self.N - df + 0.5) / (df + 0.5))
            score += (idf * (tf * (self.k1 + 1)) / 
                          (tf + self.k1 * (1 - self.b + (self.b * length / self.avg_len))))
        return score
    
    def query(self, *query, n=10):
        """Query an indexed collection. Returns a ranked list of doc ID's sorted by
        the computation of Okapi BM25."""
        if not self._all_set:
            self.df = self._document_frequency()
            self.avg_len = sum(self.lengths.values()) / self.N
            self._all_set = True
            
        scores = {doc_id: self.score(doc_id, *query) for doc_id in self.doc_ids}
        return sorted(scores.items(), key=lambda i: i[1], reverse=True)[:n]
    
    def present(self, results):
        "Present the query results as a list."
        for doc_id, score in results:
            print("%5.2f | %s" % (100 * score, doc_id))
            
    def present_results(self, *query):
        "Query the collection and present the results."
        return self.present(self.query(*query))
```

I have taken the liberty to make some minor adjustments to the class and add some methods to present the results of a query. The method `score` implements Okapi BM25 quite straightforwardly. Note that I added a boolean attribute called `_all_set` to the class. This attribute tells the system whether all the pieces of information to compute the Okapi BM25 scores have been collected. In the method `query` we ask whether all is set. If not, we first compute the document frequencies of each unique term in our collection as well as the average document length. The reason I do not compute this earlier is that after a document has been added to the index, we need to recompute all these values (note that we set `_all_set` in `index_document` to `False`). Since we do not know whether a user of this class will add some more documents after having indexed a complete collection earlier, it is safer to postpone these computations. The methods `present` and `present_results` are two helper methods to more conveniently print the results of a query.

Let's test out IR System!


```python
s = IRSystem()
s.index_collection(glob.glob('data/haggard/*.txt'))
```


```python
s.present_results("regeneration", "pharao", "odds")
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

