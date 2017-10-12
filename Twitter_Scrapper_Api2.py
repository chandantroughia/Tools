import sys 
import tweepy
from tweepy import OAuthHandler
import json
from time import sleep
from pprint import pprint           #This will print the file in a nested way. 


def make_Api():
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
 
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
 
        api = tweepy.API(auth)
        return api



def makeJson(twitterHandle, filename):
        api = make_Api()
        if twitterHandle == '@TechnicallyWise':
                troughia_tweets = []
        
                for tweet in tweepy.Cursor(api.user_timeline, id = twitterHandle).items(twitter_cutoff):
                        troughia_tweets.append(tweet._json)
                        sleep(sleep_interval)
        
                f_json = open(filename, "w")
                f_json.write(json.dumps(troughia_tweets))
                f_json.close()
                
        elif twitterHandle == '@DeepLearningHub':
                DeepLearningHub_tweets = []
        
                for tweet in tweepy.Cursor(api.user_timeline, id = twitterHandle).items(twitter_cutoff):
                        DeepLearningHub_tweets.append(tweet._json)    
                        sleep(sleep_interval)
        
                f_json = open(filename, "w")
                f_json.write(json.dumps(DeepLearningHub_tweets))
                f_json.close()
        
        elif twitterHandle == '@tensorflow':
                tensorflow_tweets = []
        
                for tweet in tweepy.Cursor(api.user_timeline, id = twitterHandle).items(twitter_cutoff):
                        tensorflow_tweets.append(tweet._json) 
                        sleep(sleep_interval)
        
                f_json = open(filename, "w")
                f_json.write(json.dumps(tensorflow_tweets))
                f_json.close()        
                
def AllInOneJson():
        api = make_Api()
        TwitterHandles = ['@tensorflow', '@DeepLearningHub', '@TechnicallyWise']
        
        all_tweets = []

        for handles in TwitterHandles:
                for tweet in tweepy.Cursor(api.user_timeline, id = handles).items(twitter_cutoff):
                        all_tweets.append(tweet._json) 
                        sleep(sleep_interval)

        f_json = open('2017-10-03-user-profiles.json', "w")
        f_json.write(json.dumps(all_tweets))
        f_json.close()        
        

if __name__ == "__main__":
        twitter_cutoff = 5 #3195
        sleep_interval = 0 #5  
        
        """Uncomment for one json file/profile
        dict = {'@tensorflow': 'tensorflow_json.json', '@DeepLearningHub': 'DeepLearningHub_json.json', '@TechnicallyWise': 'Chandan_Troughia_json.json'}
        For i in dict:
                #makeJson(i, dict[i])"""
                
                
        #All in one json
        AllInOneJson()
        
        filename='2017-10-03-user-profiles.json'
        path='./'+filename
        names=[]
        urls=[]
        
        
        with open(path) as data_file:   #The "with" incorporates an open and close of file.   
                for line in data_file:
                        #pprint(line)
                        j = json.loads(line)
                        #pprint(j)
                        #sys.exit('listofitems not long enough')
                        #names.append(j['name'])
                        #urls.append(j['url'])        
        #print(names)