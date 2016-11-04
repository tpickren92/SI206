# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


import requests
import requests_oauthlib
import json
import operator



def twitterREST():
    twitter_client_key = "TF0PtP0O9emktHIz6nE3gba3L" 
    twitter_client_secret = '3GyhZPJbimHu3hfhmpE2nJw7VAZSHA78LL3QCon0TpGvw8j6nw'

    twitter_oauth = requests_oauthlib.OAuth1Session(twitter_client_key, client_secret=twitter_client_secret)

    search_params = {}
    search_params['q'] = "#" + user_hashtag
    search_params['count'] = 20
    search_params['lang'] = 'en' 
    search_params['result_type'] = 'mixed'

    twitter_r = twitter_oauth.get("https://api.twitter.com/1.1/search/tweets.json", params = search_params) 

    twitter_res = twitter_r.json()

    #print "Caching Twitter data..."
    f = open('nestedtwitter.txt', 'w') # create empty nestedtwitter.txt
    f.write(json.dumps(twitter_res)) # load json formatted dictionary into nestedtwitter.txt
    f.close()
    #print 'Twitter data cached.'

    fref = open("nestedtwitter.txt","r")
    fstr = fref.read() # turn nestedtwitter.txt into single string
    twitter_data = json.loads(fstr) # usuable json dictionary of all the cached data

    test.testEqual(str(twitter_r), '<Response [200]>') # test if request is going through
    test.testEqual(twitter_res, twitter_data) # test if both json dictionaries match

    return twitter_data
    
