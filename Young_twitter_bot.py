# -*- coding: utf-8 -*-

import tweepy                    #important package for twitter automation!!! enter this -'pip install tweepy' in your CMD

consumer_key = ''                #for these keys, you've to apply for twitter api by creating twitter app in twitter dev. section.
consumer_secret = ''             #go to app.twitter.com / and you should have a twitter account for that.
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)    #this will print your twitter id.

def No_of_RT():
    
    search = ("python")          #only those tweets will be RTed which includes python.
              
    numberofTweets = int(input("Enter the number of RT: "))  #you can directly enter the number like 2 or 3 instead of user input
    
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        
        try:
            
            tweet.retweet()
            print("Successful")
            
            
        except tweepy.TweepError as e:
            print(e.reason)
            
        except StopIteration:
            break
        
No_of_RT()
