# In this assignment you must do a Twitter search on any term of your choice.

# Deliverables:
# 1) Print each tweet 
# 2) Print the average subjectivity of the results 
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo. 

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

public_tweets = api.search('UMSI') #enter search term here

avgsub = 0 #these all need to be added to to calculate averages at end
avgpol = 0
count = 0 

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text) #gets data for subjectivity, polarity, etc.
	tweetsub = analysis.subjectivity
	tweetpol = analysis.polarity
	count += 1
	avgsub += tweetsub
	avgpol += tweetpol
	print("Tweet Subjectivity: ", tweetsub)
	print("Tweet Polarity: ", tweetpol)

print
print("Average Subjectivity: ", (avgsub / count))
print("Average Polarity: ", (avgpol / count))