import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 

## Ask user who to search and how many posts they want 
input_id = str(input("Enter user name to search: @"))
input_count = str(input("Enter how many tweets to return: "))

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

        print(self.all_retweets)
        print("all retweets ^^^^^^")            

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        

h = twitterREST(input_id, input_count)
print(h.twitterCall())


