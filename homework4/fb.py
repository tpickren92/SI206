# import urllib
# # import urllib2
# from urllib.request import urlopen
# import requests
# import requests_oauthlib
# import json
# import datetime
# import csv
# import time


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

# page_id = input("Enter a user to search: ")
page_id = "diplo"



def request_until_succeed(url):
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


# Needed to write tricky unicode correctly to csv
def unicode_normalize(text):
    return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22,
                            0xa0:0x20 })

def getFacebookPageFeedData(page_id, access_token, num_statuses):

    # Construct the URL string; see http://stackoverflow.com/a/37239851 for
    # Reactions parameters
    base = "https://graph.facebook.com/v2.6"
    node = "/%s/posts" % page_id 
    fields = "/?fields=message,link,created_time,type,name,id," + \
            "comments.limit(0).summary(true),shares,reactions" + \
            ".limit(0).summary(true)"
    parameters = "&limit=%s&access_token=%s" % (num_statuses, access_token)
    url = base + node + fields + parameters

    # retrieve data
    data = json.loads(request_until_succeed(url))

    return data
    

test_status = getFacebookPageFeedData(page_id, access_token, 5)["data"]#[0]

# print(test_status)
print (json.dumps(test_status, indent=4, sort_keys=True))