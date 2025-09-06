
<BR>

|:-------:|
| <span style="font-size: 100%"><b>_-- A Python Course for the Humanities by Folgert Karsdorp and Maarten van Gompel_</b></span>|

# Extracting a social network of Twitter users

Now we will turn to the practical assignment of this chapter. The extraction of a graph of who tweets whom. For this purpose we make available the dataset [twitterdata.zip](http://lst.science.ru.nl/~proycon/twitterdata.zip) , download and extract it in a location of your choice.

The program we are writing will consist of three classes: `Tweet`,`TweetUser` and `TweetGraph`. `TweetGraph` will maintain a dictionary of users (`TweetUser`), these are the nodes of our graph. `TweetUser` will in turn maintain a list of tweets (`Tweet`). `TweetUser` will also maintain a dictionary in which the keys are other TweetUser instances and the values indicate the weight of the relationship. This thus makes up the edges of our graph.

You will not have to write everything from scratch, we will provide a full skeleton in which you have to implement certain methods. We are going to use our external editor for this assignment. Copy the below code, edit it, and save it as `tweetnet.py`. When done, run the program from the command line, passing it one parameter, the directory where the *txt files from twitterdata.zip can be found: *python3 tweetnet.py /path/to/twitterdata/*


```python
#! /usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import preprocess


class Tweet:    
    def __init__(self, message, time):
        self.message = message
        self.time = time
        

class TwitterUser:
    def __init__(self, name):
        self.name = name
        self.tweets = [] #This will be a list of all tweets 
        self.relations = {} #This will be a dictionary in which the keys are TwitterUser objects and the values are the weight of the relation (an integer) 
    
    def append(self, tweet):
        assert isinstance(tweet, Tweet) #this is a test, if tweet is not an instance
                                        #of Tweet, it will raise an Exception.
        self.tweets.append(tweet)
        
    def __iter__(self):
        #This function, a generator, should iterate over all tweets
        #<INSERT YOUR CODE HERE>
        
    
    def __hash__(self):    
        #For an object to be usable as a dictionary key, it must have a hash method. Call the hash() function over something that uniquely defined this object
        #and thus can act as a key in a dictionary. In our case, the user name is good, as no two users will have the same name:          
        return hash(self.name)
    
    
    def addrelation(self, user):
        if user and user != self.name: #user must not be empty, and must not be the user itself
            if user in self.relations:
                #the user is already in our relations, strengthen the bond:
                self.relations[user] += 1
            elif user in graph:                        
                #the user exists in the graph, we can add a relation!
                self.relations[user] = 1
            #if the user does not exist in the graph, no relations will be added        
        
    
    def computerelations(self, graph):
        for tweet in self:
            #tokenise the actual tweet content (use the tokeniser in preprocess!):
            tokens = #<INSERT YOUR CODE HERE>
            
            #Search for @username tokens, extract the username, and call self.addrelation()
            #<INSERT YOUR CODE HERE>
        
        
    def printrelations(self):
        #print the relations, include both users and the weight
        #<INSERT YOUR CODE HERE>
 
        
    def gephioutput(self): 
        #produce CSV output that gephi can import
        for recipient, weight in self.relations.items():
            for i in range(0, weight):
                yield self.name + "," + recipient
 
        
class TwitterGraph:
    def __init__(self, corpusdirectory):        
        self.users = {} #initialisation of dictionary that will store all twitter users. They keys are the names, the values are TwitterUser objects.
                        #the keys are the usernames (strings), and the values are
                        # TweetUser instances
                
        #Load the twitter corpus 
        #tip: use preprocess.find_corpusfiles and preprocess.read_corpus_file,
        #do not use preproces.readcorpus as that will include sentence segmentation
        #which we do not want
        
        #Each txt file contains the tweets of one user.
        #all files contain three columns, separated by a TAB (\t). The first column
        #is the user, the second the time, and the third is the tweetmessage itself.
        #Create Tweet instances for every line that contains a @ (ignore other lines 
        #to conserve memory). Add those tweet instances to the right TweetUser. Create
        #TweetUser instances as new users are encountered.
        
        #self.users[user], which user being the username (string), should be an instance of the
        #of TweetUser
        
        #<INSERT YOUR CODE HERE>

            
        #Compute relations between users
        for user in self:
            assert isinstance(user,TweetUser)
            user.computerelations(self)
    

    
    def __contains__(self, user):
        #Does this user exist?
        return user in self.users
    
    def __iter__(self):
        #Iterate over all users
        for user in self.users.values():
            yield user

    def __getitem__(self, user):    
        #Retrieve the specified user
        return self.users[user]
            

#this is the actual main body of the program. The program should be passed one parameter
#on the command line: the directory that contains the *.txt files from twitterdata.zip.

#We instantiate the graph, which will load and compute all relations
twittergraph = TwitterGraph(sys.argv[1])

#We output all relations:
for twitteruser in twittergraph:
    twitteruser.printrelations()

#And we output to a file so you can visualise your graph in the program GEPHI
f = open('gephigraph.csv','wt',encoding='utf-8')
for twitteruser in twittergraph:
    for line in twitteruser.gephioutput(): 
        f.write(line + "\n")
f.close()
```

<BR>

----

[Python Programming for the Humanities](http://fbkarsdorp.github.io/python-course) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). Based on a work at https://github.com/fbkarsdorp/python-course.

![Creative Commons](../graphics/CreativeCommons.png)

