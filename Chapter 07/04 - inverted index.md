
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Inverted Index

The *Inverted Index* is *the* key data structure in modern Information Retrieval. An inverted index is a structure in which for each unique term $t$ in our collection, we store a list of all document ID's that contain $t$. If we represent our small collection of newspapers in this way, it looks like this:

`Einstein: [12-11-1928, 04-04-1946]`   
`Hubble:   [12-11-1928, 04-04-1946, 03-11-1983]`   
`Fermi:    [12-11-1928]`   
`Winfrey:  [19-01-1999]`   
`Dylan:    [03-11-1983, 19-01-1999]`

# Quiz!

1. What would be a convenient and efficient data structure in Python to represent an inverted index?

    * Double click this cell and write down your answer.*

2.  We will implement a first version of an IR system. I choose to implement it as the class `IRSystem`. Implement the method `index_document`. It takes as argument a document ID and a list of words. The function should update the variable `tdf` in such a way that for each term it stores a set of all document IDs in which that term occurs.

    ```python
    import glob, os, re
    from collections import defaultdict


    def tokenize(text, lowercase=True):
        text = text.lower() if lowercase else text
        for match in re.finditer(r"\w+(\.?\w+)*", text):
            yield match.group()

            
    class IRSystem:
        """A very simple Information Retrieval System. The constructor 
        s = IRSystem() builds an empty system. Next, index several documents 
        with s.index_document(ID, text).
        """
        
        def __init__(self):
            "Initialize an IR Sytem."
            self.tdf = defaultdict(set)
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
        
    # these tests should return True if your code is correct
    s = IRSystem()
    s.index_collection(glob.glob('data/haggard/*.txt'))

    print('The Ghost Kings 8184.txt' in s.tdf['master'])
    print('Cleopatra 2769.txt' in s.tdf['children'])
    ```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

