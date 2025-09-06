
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Term Document Incidence Matrix

To efficiently give an answer to such queries we need to come up with another representation of our collection instead of plain text. Have a look at the following table.

<BR>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>12-11-1928</th>
      <th>04-04-1946</th>
      <th>03-11-1983</th>
      <th>19-01-1999</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Einstein</th>
      <td> 1</td>
      <td> 1</td>
      <td> 0</td>
      <td> 0</td>
    </tr>
    <tr>
      <th>Hubble</th>
      <td> 1</td>
      <td> 1</td>
      <td> 1</td>
      <td> 0</td>
    </tr>
    <tr>
      <th>Fermi</th>
      <td> 1</td>
      <td> 0</td>
      <td> 0</td>
      <td> 0</td>
    </tr>
    <tr>
      <th>Winfrey</th>
      <td> 0</td>
      <td> 0</td>
      <td> 0</td>
      <td> 1</td>
    </tr>
    <tr>
      <th>Dylan</th>
      <td> 0</td>
      <td> 0</td>
      <td> 1</td>
      <td> 1</td>
    </tr>
  </tbody>
</table>

<BR>

This table is called a *Term Document incidence matrix* where for each term (rows) we write down a 1 if a particular document (columns) contains that term and 0 otherwise. In this representation each term is represented by an incidence vector. If we want to extract all documents that mention Albert Einstein, we can use the binary vector `1100` of Einstein to quickly extract all documents mentioning Einstein. To find all documents containing both Einstein and Hubble we take the complement of the vectors of Einstein (1100) and Hubble (1110):

`1100 AND 1110 = 1100`   

# Quiz!

1. Given the incidence vectors of Einstein (1100), Hubble (1110) and Fermi (1000), what is the binary representation corresponding to the query `Einstein AND Hubble AND NOT Fermi`?

    * Double click this cell and write down your answer.*

2. Can you implement the function `AND` that takes as argument two incidence vectors (represented a binary lists in Python) and returns the complement of the two?


    ```python
    def AND(vector_a, vector_b):
        # insert your code here
        
    # these tests should return True if your code is correct
    print(AND([1, 1, 0, 0], [1, 1, 1, 0]) == [1, 1, 0, 0])
    print(AND([1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1]) == [1, 0, 0, 0, 0, 0, 1])
    ```

3. Rewrite the function `AND` to allow it to take an arbitary number of incidence vectors.

    ```python
    def AND(*vectors):
        # insert your code here    

    # these tests should return True if your code is correct
    print(AND([1, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0]) == [1, 0, 0, 0])
    print(AND([1, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 1, 0, 1]) == [0, 0, 0, 0, 0])
    ```

4. Implement the function `NOT`. It takes as argument an incidence vector and returns a representation that can be used in combination with AND queries.

    ```python
    def NOT(vector):
        # insert your code here

    # these tests should return True if your code is correct
    print(AND([1, 1, 0, 0], [1, 1, 1, 0], NOT([1, 0, 0, 0])) == [0, 1, 0, 0])
    ```

<BR>

The binary representation allows us to efficiently search for documents containing particular terms of a search query. There are, however, still some problems that need to be overcome. Consider a document collection of 1 million documents where each document is about a thousand words long. On average such a collection contains approximately 500k unique terms. This means that if we try to build an incidence matrix, we would have to construct a matrix containing $500,000 \times 1,000,000 =$ half a trillion 0's and 1's. Such a large matrix cannot be stored on a simple laptop.

# Quiz!

1. Much of the information in the matrix is redundant. Why?

    * Double click this cell and write down your answer.*

2. What would be a better representation of our matrix?

    * Double click this cell and write down your answer.*

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

