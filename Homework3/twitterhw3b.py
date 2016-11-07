# In this assignment you must do a Twitter search on any term of your choice.

# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

# print("Average subjectivity is")
# print("Average polarity is")

import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob

consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
public_tweets = api.search('UMSI')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print("Subjectivity", analysis.subjectivity)
	print("Polarity ", analysis.polarity)
	print
	
#to find polarity/subjectivity https://github.com/redsky17/TwitterPersonality
# python twitter-persona.py [redacted_key] [redacted_secret] "Macklemore" 500 False
