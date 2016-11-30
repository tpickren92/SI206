import tweepy
import nltk
import requests
import requests_oauthlib
import urllib.request
import json
from textblob import TextBlob
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 
import numpy as np
import matplotlib.pyplot as plt

## Ask user who to search and how many posts they want 
# input_id = str(input("Enter user name to search: @"))
# input_count = str(input("Enter how many tweets to return: "))
input_id = 'diplo'
input_count = 20

## need rest class for twitter and fb, then both of those are inherited by graphing class
## structure of tweepy objec - http://tkang.blogspot.com/2011/01/tweepy-twitter-api-status-object.html
    ## -http://stackoverflow.com/questions/15628535/how-can-i-retrieve-all-tweets-and-attributes-for-a-given-user-using-python

class twitterREST():
    def __init__(self, input_id, input_count): #when instance is created, requires id and count
        self.input_id = input_id
        self.input_count = input_count

    #### ASK ABOUT SECRET.PY
    def twitterCall(self):
        self.consumer_key = "jZwCk43jJnWbi9TwiqcUlZZDs" 
        self.consumer_secret = "sE9nHKucq2XA708lNmp5Mw70BFCIE7NKzDhbdsVVbyzwCZX2PI"
        self.access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
        self.access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret) #standard api call 
        auth.set_access_token(self.access_token,self.access_token_secret)
        api = tweepy.API(auth)
        
        search_user = api.user_timeline(id=self.input_id, count=self.input_count) #return user defined items

        print("Here are {}'s last {} tweets: ".format(self.input_id,self.input_count))
        print("")

        self.number_of_retweets = 0
        self.all_retweets = []

        for tweet in search_user:
            print ("Text:", tweet.text) #tweet content
            print ("Created:", tweet.created_at) #time of creation
            if tweet.retweet_count:
                self.number_of_retweets = tweet.retweet_count
                self.all_retweets.append(self.number_of_retweets)
                print ("Retweet count:", tweet.retweet_count)
            else:
                self.number_of_retweets = 0
                self.all_retweets.append(self.number_of_retweets)
                print("No retweets")

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        
    
class fbREST():
    def __init__(self, input_id, input_count): #when instance is created, requires id and count
        self.input_id = input_id
        self.input_count = input_count

    def fbCall(self):
        app_id = "1798098537096839" #standard call
        app_secret = "6d77ad9d68559dee924b923f27b65499" 
        access_token = app_id + "|" + app_secret

        base = "https://graph.facebook.com/v2.6" #construct url
        node = "/%s/posts" % input_id 
        fields = "/?fields=message,link,created_time,type,name,id," + \
                "comments.limit(0).summary(true),shares,reactions" + \
                ".limit(0).summary(true)"
        parameters = "&limit=%s&access_token=%s" % (input_count, access_token)
        url = base + node + fields + parameters

        req = urllib.request.Request(url) #make request
        response = urllib.request.urlopen(req)
        response = response.read().decode(response.headers.get_content_charset())

        data = json.loads(response)
        data = data['data'] # ignore messy message ids

        self.share_count = 0
        self.all_shares = []
        for post in data:
            print(post["message"])
            print(post["created_time"])
            if "shares" in post:
                self.share_count = post["shares"]["count"]
                self.all_shares.append(self.share_count)
                print(self.all_shares)
            else:
                self.share_count = 0 
                self.all_shares.append(self.share_count)
                print("No shares")
        return data

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        


class Graphing(twitterREST,fbREST):
    def __init__(self):
        twitterREST.__init__(self, input_id, input_count)
        twitterREST.twitterCall(self)
        print(self.all_retweets)
        print("all retweets ^^^^^^^^^^^^^^^^")            
        fbREST.__init__(self, input_id, input_count)
        fbREST.fbCall(self)
        print(self.all_shares)
        print("All shares ^^^^^^^^^^^")

        N = int(input_count)
        ##all_shares = [190, 325, 130, 135, 427] # share/retweet count - used to be tuple but that isnt needed?
        # menStd = (2, 3, 4, 1, 2) #dont need

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, self.all_shares, width, color='b')
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height), ha='center', va='bottom')

        ##all_retweets = [125, 202, 314, 120, 250]
        # womenStd = (3, 5, 2, 3, 3)
        rects2 = ax.bar(ind + width, self.all_retweets, width, color='y')
        for rect in rects2:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height), ha='center', va='bottom')


        # add some text for labels, title and axes ticks
        ax.set_ylabel('Number of Shares/Retweets of') #nice to have username added here
        ax.set_title('Share/Retweet comparison')
        ax.set_xticks(ind + width)

        empty = []
        count = 1
        for x in range(input_count):
            empty.append("Post "+str(count))
            count += 1

        ax.set_xticklabels(empty,rotation=45) #how to include time of creation? - need to adjust for number inputting

        ax.legend((rects1[0], rects2[0]), ('Facebook', 'Twitter')) #key text

        plt.show()


f = fbREST(input_id,input_count)
fb_status = f.fbCall()

t = twitterREST(input_id, input_count)
twitter_status = t.twitterCall()

g = Graphing()

