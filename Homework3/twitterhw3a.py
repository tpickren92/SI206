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

access_token = "36224295-icFWtb45o6oGSQlNow89Zon1dk3ezUPpfyoRZ9W1L"
access_token_secret = "rb5sUyzZlQIbXQHnCoprBkxWdOethWw8goL0Qtc1A1onT"
consumer_key = "Pixu7snuSdcO5wHpgPcFdZznu"
consumer_secret = "3Oi9q76CZ9D5x0ULSdDKB1zydHqynTkPK1ockJCnEkwA5fRWlR"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img = "insert here"
api.update_with_media(img, status="#UMSI-206 #Proj3")
print("posted")