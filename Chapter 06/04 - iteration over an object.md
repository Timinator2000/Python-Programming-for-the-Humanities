
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Iteration Over an Object

Remember how we can iterate over lists and dictionaries using a for loop? To recap:

```python
fruits = ['banana','pear','orange']
for fruit in fruits:
    print(fruit)
```

We can do the same for our own object. We can make them support iteration. This is done by overloading the `__iter__` method. It takes no extra arguments and should be a **generator**. Which if you recall means that you should use `yield` instead of `return`. Consider the following class `TwitterUser`, if we iterate over an instance of that class, we want to iterate over all tweets. To make it more fun, let's iterate in chronologically sorted order:


```python
class TwitterUser:
    def __init__(self, name):
        self.name = name
        self.tweets = [] #This will be a list of all tweets, these should be Tweet objects
    
    def append(self, tweet):
        assert isinstance(tweet, Tweet) #this code will check if tweet is an instance
                                        #of the Tweet class. If not, an exception
                                        #will be raised
        #append the tweet to our list
        self.tweets.append(tweet)
        
    def __iter__(self):
        for tweet in sorted(self.tweets):
            yield tweet

        
tweeter = TwitterUser("proycon")
tweeter.append(Tweet("My peanut butter sandwich has just fallen bottoms-down",4)) 
tweeter.append(Tweet("Tying my shoelaces",2)) 
tweeter.append(Tweet("Wiggling my toes",3)) 
tweeter.append(Tweet("Staring at a bird",1)) 

for tweet in tweeter:
    print(tweet.message)
```

# Exercise

The method `__len__` is invoked when the built-in function `len()` is used. We want it to return the number of tweets a user has. Implement it in the example above and then run the following test, which should return `True` if you did well:

```python
print(len(tweeter) == 4)
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

