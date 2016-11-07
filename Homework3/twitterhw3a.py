# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
    can print out a success/failure message if you want to.""")

import tweepy
import nltk
import requests
import requests_oauthlib

consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img = "/Users/tom/projects/SI206/Homework3/media/football.jpg"  # ask about file path
api.update_with_media(img, status=" Testing... #UMSI-206 #Proj3")
print("Posted")

