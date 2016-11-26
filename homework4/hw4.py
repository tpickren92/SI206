
import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 

# consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
# consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
# access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
# access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)
# api = tweepy.API(auth)

input_id = str(input("Enter user name to search: @"))
input_count = str(input("Enter how many tweets to return: "))

# search_user = api.user_timeline(id=input_id, count=input_count)

# print('Here are the last 5 tweets: ')
# for x in search_user:
#     print("")
#     print(x.text)
#     print(x.id)
#     print(x.favorited)
#     print(x.retweeted)
#     print(x.retweet_count)
#     print(x.favorite_count)


## need rest class for twitter and fb, then both of those are inherited by graphing class
## structure of tweepy objec - http://tkang.blogspot.com/2011/01/tweepy-twitter-api-status-object.html
    ## -http://stackoverflow.com/questions/15628535/how-can-i-retrieve-all-tweets-and-attributes-for-a-given-user-using-python

class twitterREST():
    def __init__(self, input_id, input_count):
        self.input_id = input_id
        self.input_count = input_count

    def twitterCall(self):
        self.consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
        self.consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
        self.access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
        self.access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        api = tweepy.API(auth)

        search_user = api.user_timeline(id=self.input_id, count=self.input_count)

        print('Here are the last 5 tweets: ')
        for tweet in search_user:
            print ("ID:", tweet.id)
            print ("User ID:", tweet.user.id)
            print ("Text:", tweet.text)
            print ("Created:", tweet.created_at)
            print ("Geo:", tweet.geo)
            print ("Contributors:", tweet.contributors)
            print ("Coordinates:", tweet.coordinates) 
            print ("Favorited:", tweet.favorited)
            print ("In reply to screen name:", tweet.in_reply_to_screen_name)
            print ("In reply to status ID:", tweet.in_reply_to_status_id)
            print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
            print ("In reply to user ID:", tweet.in_reply_to_user_id)
            print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
            print ("Place:", tweet.place)
            print ("Retweeted:", tweet.retweeted)
            print ("Retweet count:", tweet.retweet_count)
            print ("Source:", tweet.source)
            print ("Truncated:", tweet.truncated)

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        



h = twitterREST(input_id, input_count)
print(h.twitterCall())


