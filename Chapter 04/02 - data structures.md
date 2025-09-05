
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Data Structures

Perhaps the most important aspect of writing good programs is developing and designing appropriate data structures for the problem at hand. Data structures should feel natural, be flexible, and should not be unnecessarily difficult or hard to read. As a rule of thumb, most of the time the least complex data structure is the one to go with. Let's have a look at a real example to see what different design choices we can make regarding data structures.

In the file `data/twitter.txt` we constructed a fictional network of twitter users. Each line represents an edge in the network between two users separated by a semicolon:

`@Fox;@Judie`

`@Tristan;@Jermain`

`@Allyn;@Winfred`

`@Dennis;@Randolph`

`@Wallie;@Venkat`

The first name represents the follower; the second name the followee. 

One seemingly natural data structure to represent this network in Python is a list of tuples each consisting of two names: `[(name1, name2), (name1, name3), ..., (name300, name41)]`. We construct the network in this format as follows: 


```python
edges = []
for line in open("data/twitter.txt"):
    name_a, name_b = line.strip().split(';')
    edges.append((name_a, name_b))
print(edges[:10])
```

In itself nothing is wrong with this data structure. For example, we might use it as follows to find all people user @Fox follows:

```python
def following(user, edges):
    "Return a list of all users USERS is following."
    followees = []
    for follower, followee in edges:
        if follower == user:
            followees.append(followee)
    return followees

print(following("@Fox", edges))
```

One particular downside of this datastructure, especially when our network grows, is that it can become slow, painstakingly slow... For each search query, we have to go through the entire network, check for each node whether it is equal to the one we're looking for and then append the followee to the list of followees. To give you an impression of how long Python is taking, execute the following cell:

```python
%timeit following("@Fox", edges)
```

It depends a little on your computer, but it will probably be around 500 microseconds per loop or 0.000592 seconds. "That's quite fast!", you might think. Just wait and see what happens if we adjust our data structure to the following. This time we represent our network as a dictionary with followers as keys and a list of followees as value. 

```python
edge_dict = {}
for line in open("data/twitter.txt"):
    name_a, name_b = line.strip().split(';')
    if name_a in edge_dict:
        edge_dict[name_a].append(name_b)
    else:
        edge_dict[name_a] = [name_b]
```

It is not really necessary to define the following function, but we'll do it just so that it is easier to compare with the previous one.


```python
def following2(user, edges):
    return edges[user]
```

Now let's test this function:


```python
%timeit following2("@Fox", edge_dict)
```

This function approximately takes about 160 nanoseconds per loop, which is around 0.000000165 seconds. Now *that* is fast! You're probably thinking that it is not really a big deal, since you can't really tell the difference. And you're right: for this particular case it doesn't really matter. But what if our network was ten times as big? Or 100 times, 1000 or a million times? Then what would happen? To convince you of my point, I'll will expand our network, making it 1000 times bigger.


```python
edges = []
for line in open("data/twitter.txt"):
    name_a, name_b = line.strip().split(';')
    # repeatedly add edges to the network (1000 times)
    for i in range(1000):
        edges.append((name_a, name_b))
```


```python
%timeit following("@Fox", edges)
```

The function has become quite a bit slower. It will be somewhere around 570 milliseconds, or 0.57 seconds. Now lets do the same thing with the dictionary network


```python
edge_dict = {}
for line in open("data/twitter.txt"):
    name_a, name_b = line.strip().split(';')
    for i in range(1000):
        if name_a in edge_dict:
            edge_dict[name_a].append(name_b)
        else:
            edge_dict[name_a] = [name_b]
```


```python
%timeit following2("@Fox", edge_dict)
```

The timing is still about the same! What's going on?! It would take too long to explain to you exactly what the difference is between a dictionary and a list (you can read more about it [here](http://en.wikipedia.org/wiki/Hash_table)), but for now you should remember that you can access keys in a dictionary in constant time (meaning it does not matter how big the dictionary is), whereas for a list, it depends on the size of the list. This example makes it clear that the choice for a given data structure can make a real difference.

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

