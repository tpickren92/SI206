import urllib.request
import json
import datetime
import csv
import time
import codecs

#### https://github.com/minimaxir/facebook-page-post-scraper/blob/master/examples/how_to_build_facebook_scraper.ipynb

app_id = "1798098537096839"
app_secret = "6d77ad9d68559dee924b923f27b65499" 
access_token = app_id + "|" + app_secret

# input_id = input("Enter a user to search: ")
input_id = "diplo"
input_count = 5


class fbREST():
    def __init__(self, input_id, access_token, input_count): #when instance is created, requires id and count
        self.input_id = input_id
        self.access_token = access_token
        self.input_count = input_count

    def request_until_succeed(self, url):
        req = urllib.request.Request(url)
        success = False
        while success is False:
            try: 
                response = urllib.request.urlopen(req)
                if response.getcode() == 200:
                    success = True
            except Exception as e:
                print(e)
                time.sleep(5)

                print("Error for URL %s: %s" % (url, datetime.datetime.now()))
                print("Retrying.")

        return response.read().decode(response.headers.get_content_charset())

    def getFacebookPageFeedData(self):   ###(self, input_id, access_token, input_count):

        # Construct the URL string; see http://stackoverflow.com/a/37239851 for
        # Reactions parameters
        base = "https://graph.facebook.com/v2.6"
        node = "/%s/posts" % input_id 
        fields = "/?fields=message,link,created_time,type,name,id," + \
                "comments.limit(0).summary(true),shares,reactions" + \
                ".limit(0).summary(true)"
        parameters = "&limit=%s&access_token=%s" % (input_count, access_token)
        url = base + node + fields + parameters

        # retrieve data
        data = json.loads(request_until_succeed(url))

        #return data

        for post in data:
            print(post["message"])
            print(post["created_time"])
            if "shares" in post:
                print(post["shares"]["count"])
            else:
                print("No shares")

    # def parseFacebookPageFeedData(self):    

    #     test_status = getFacebookPageFeedData(input_id, access_token, 5)["data"]

    #     for post in test_status:
    #         print(post["message"])
    #         print(post["created_time"])
    #         if "shares" in post:
    #             print(post["shares"]["count"])
    #         else:
    #             print("No shares")

    
t = fbREST(input_id, access_token, input_count)
print(t.getFacebookPageFeedData())

# test_status = getFacebookPageFeedData(input_id, access_token, 5)["data"]

# for post in test_status:
#     print(post["message"])
#     print(post["created_time"])
#     if "shares" in post:
#         print(post["shares"]["count"])
#     else:
#         print("No shares") # should create shares key in dictionary with count of 0?

# print (json.dumps(test_status, indent=4, sort_keys=True)) #to view original json with nesting 