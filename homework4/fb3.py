import urllib.request
import json

#### https://github.com/minimaxir/facebook-page-post-scraper/blob/master/examples/how_to_build_facebook_scraper.ipynb

input_id = "diplo"
input_count = 3
    
class fbREST():
    def __init__(self, input_id, input_count): #when instance is created, requires id and count
        self.input_id = input_id
        self.input_count = input_count

    def fbCall(self):
        app_id = "1798098537096839" #standard call
        app_secret = "6d77ad9d68559dee924b923f27b65499" 
        access_token = app_id + "|" + app_secret

        base = "https://graph.facebook.com/v2.6" #construct url
        node = "/%s/posts" % input_id 
        fields = "/?fields=message,link,created_time,type,name,id," + \
                "comments.limit(0).summary(true),shares,reactions" + \
                ".limit(0).summary(true)"
        parameters = "&limit=%s&access_token=%s" % (input_count, access_token)
        url = base + node + fields + parameters

        req = urllib.request.Request(url) #make request
        response = urllib.request.urlopen(req)
        response = response.read().decode(response.headers.get_content_charset())

        data = json.loads(response)
        data = data['data'] # ignore messy message ids

        self.share_count = 0
        self.all_shares = []
        for post in data:
            print(post["message"])
            print(post["created_time"])
            if "shares" in post:
                self.share_count = post["shares"]["count"]
                self.all_shares.append(self.share_count)
                print(self.all_shares)
                print("shares ^^^^^^")
            else:
                self.share_count = 0 
                self.all_shares.append(self.share_count)
                print("No shares")

        return data

    def __str__(self):
        return "The user chosen id is {} and the number of posts is {}.".format(self.input_id,self.input_count)        


f = fbREST(input_id,input_count)
test_status = f.fbCall()
print(f.__str__())
