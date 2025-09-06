
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Operator Overloading

If you write your own classes, you can define what needs to happen if an operator such as for example `+`,`/` or `<` is used on your class. You can also define what happens when the keyword `in` or built-in functions such as `len()` are you used with your class. This allows for a very elegant way of programming. Each of these operators and built-in functions have an associated method which you can overload. All of these methods start, like `__init__`, with a double underscore.

For example. Let's allow comparison of tweets using the '<' and '>' operators. The methods for the opertors are respectively `__lt__` and `__gt__`, both take one argument, the other object to compare to. A tweet qualifies as greater than another if it is a newer, more recent, tweet:

```python
class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time # we will assume here that time is a numerical value
        
    def __lt__(self, other):
        return self.time < other.time
        
    def __gt__(self, other):
        return self.time > other.time    
    

oldtweet = Tweet("this is an old tweet",20)
newtweet = Tweet("this is a new tweet",1000)
print(newtweet > oldtweet)     
```

You may not yet see much use in this, but consider for example the built-in function `sorted()`. Having such methods defined now means we can sort our tweets! And because we defined the methods `__lt__` and `__gt__` based on time. It will automatically sort them on time, from old to new:

```python
tweets = [newtweet,oldtweet]

for tweet in sorted(tweets):
    print(tweet.message)
```

# Exercise

Remember the `in` keyword? Used checking items in lists and keys in dictionaries? To recap:


```python
fruits = ['banana','pear','orange']
print('pear' in fruits)
```

Overloading this operator is done using the `__contains__` method. It takes as extra argument the item that is being searched for ('pear' in the above example). The method should return a boolean value. For tweets, let's implement support for the `in` operator and have it check whether a certain word is in the tweet.

```python
class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time

    def __lt__(self, other):
        return self.time < other.time
        
    def __contains__(self, word):
        #Implement the method

tweet = "I just flushed my toilet"
#now write code to check if the word "flushed" is in the tweet
#and print something nice if that's the case
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

