import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import sys 
import tweepy

from time import sleep
from pprint import pprint           #This will print the file in a nested way. 


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = OAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_token, access_token_secret)

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
#search
api = tweepy.API(auth)
twitterStream = Stream(auth,TweetListener())
nameList = []
nameList.append(api.get_user(screen_name = 'tensorflow'))
nameList.append(api.get_user(screen_name = 'DeepLearningHub'))
nameList.append(api.get_user(screen_name = 'TechnicallyWise'))

allData = []
for user in nameList:
    allData.append(user._json)

f_json = open('2017-10-03-user-profiles.json', "w")
f_json.write(json.dumps(allData))
f_json.close()

filename='2017-10-03-user-profiles.json'
path='./'+filename
names=[]
urls=[]


with open(path) as data_file:   #The "with" incorporates an open and close of file.   
        for line in data_file:
                j = json.loads(line)
                for i in j:
                    names.append(i['name'])
                    urls.append(i['url'])
                      
print(names)
print(urls)