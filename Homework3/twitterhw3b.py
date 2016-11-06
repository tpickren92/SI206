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

access_token = "36224295-icFWtb45o6oGSQlNow89Zon1dk3ezUPpfyoRZ9W1L"
access_token_secret = "rb5sUyzZlQIbXQHnCoprBkxWdOethWw8goL0Qtc1A1onT"
consumer_key = "Pixu7snuSdcO5wHpgPcFdZznu"
consumer_secret = "3Oi9q76CZ9D5x0ULSdDKB1zydHqynTkPK1ockJCnEkwA5fRWlR"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
public_tweets = api.search('UMSI')

for tweet in public_tweets:
	print(tweet.text)
	
