
import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 

consumer_key = "nMmbMhqAl4SORXjcUOyPDdMbo"
consumer_secret = "Q5gbSQGjD4BqLwSxWh0JhGORMWmmHzMcWHG3zWGUzHs2fL0ucG"
access_token = "795658546063044608-xZEMs8fFAuI0Uc85RBWr39DGZKtoWGw"
access_token_secret = "vO4B9fUIdM3kcivVgg2EU7ZAq53ZapX0C9zDquUuMHlLy"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

input_id = str(input("Enter user name to search: @"))
input_count = str(input("Enter how many tweets to return: "))

search_user = api.user_timeline(id=input_id, count=input_count)

print('Here are the last 5 tweets: ')
for x in search_user:
    print("")
    print(x.text)
    print(x.id)
    print(x.favorited)
    print(x.retweeted)
    print(x.retweet_count)
    print(x.favorite_count)


# search_user = search_user.json()
# print(type(search_user))
# text_file = open("Hw4TwitterOutput.json", "w")
# print('Outputting json file....')
# text_file.write(str(search_user))
# text_file.close()
# print('Done')


# public_tweets = api.search('UMSI') #enter search term here

# avgsub = 0 #these all need to be added to to calculate averages at end
# avgpol = 0
# count = 0 

# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text) #gets data for subjectivity, polarity, etc.
#     tweetsub = analysis.subjectivity
#     tweetpol = analysis.polarity
#     count += 1
#     avgsub += tweetsub
#     avgpol += tweetpol
#     print("Tweet Subjectivity: ", tweetsub)
#     print("Tweet Polarity: ", tweetpol)

# print
# print("Average Subjectivity: ", (avgsub / count))
# print("Average Polarity: ", (avgpol / count))

# class StdOutListener(StreamListener):
#     """ A listener handles tweets that are received from the stream.
#     This is a basic listener that just prints received tweets to stdout.
#     """
#     def on_data(self, data):
#         print(data)
#         return True

#     def on_error(self, status):
#         print(status)

# if __name__ == '__main__':
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)

#     stream = Stream(auth, l)
#     stream.filter(track=['basketball'])