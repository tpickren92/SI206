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

    def twitterCall(self):
        self.consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
        self.consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
        self.access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
        self.access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret) #standard api call 
        auth.set_access_token(self.access_token,self.access_token_secret)
        api = tweepy.API(auth)

        search_user = api.user_timeline(id=self.input_id, count=self.input_count) #return user defined items

        print("Here are {}'s last {} tweets: ".format(self.input_id,self.input_count))
        print("")
        
        for tweet in search_user:
            # print ("ID:", tweet.id)
            # print ("User ID:", tweet.user.id)
            print ("Text:", tweet.text) #tweet content
            print ("Created:", tweet.created_at) #time of creation
            # print ("Geo:", tweet.geo)
            # print ("Contributors:", tweet.contributors)
            # print ("Coordinates:", tweet.coordinates) 
            # print ("Favorited:", tweet.favorited)
            # print ("In reply to screen name:", tweet.in_reply_to_screen_name)
            # print ("In reply to status ID:", tweet.in_reply_to_status_id)
            # print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
            # print ("In reply to user ID:", tweet.in_reply_to_user_id)
            # print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
            # print ("Place:", tweet.place)
            # print ("Retweeted:", tweet.retweeted)
            print ("Retweet count:", tweet.retweet_count)
            # print ("Source:", tweet.source)
            # print ("Truncated:", tweet.truncated)

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        



h = twitterREST(input_id, input_count)
print(h.twitterCall())


