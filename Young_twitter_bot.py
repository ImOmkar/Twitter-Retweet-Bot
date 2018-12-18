# -*- coding: utf-8 -*-

import tweepy

consumer_key = 'maxjGQ41GxmdC8qQX0qNP7yn3'
consumer_secret = 'ZI71K676lOsFjdfPcPZDt2Q3l7TuTgWNZkjW5fx4x13slyjfr2'
access_token = '2916679106-kX4HEGa25wM14xz8xwCjSlXUez1HLY2pZ0inIxo'
access_token_secret = 'u0cFW727dAueMizh7J5gIymAkOHVwgr4t3IF6yuBxfXQV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def No_of_RT():
    
    search = ("#KanganaRanaut")
              
    numberofTweets = int(input("Enter the number of RT: "))
    
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        
        try:
            
            tweet.retweet()
            print("Successful")
            
            
        except tweepy.TweepError as e:
            print(e.reason)
            
        except StopIteration:
            break
        
No_of_RT()
