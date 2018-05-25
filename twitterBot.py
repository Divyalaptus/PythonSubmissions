#!python
# -*- coding: utf-8 -*-

"""
Created on Sat May  5 21:56:21 2018

@author: Divyalaptus
"""

API_KEY = 'kkenwjUWEQdlDWNU4PaJOJmvO'
API_SECRET = 'mOYUSYXqz4rKyIkDH5P6QCOXq8pjdOAVRSLEiTRue3KLXs86xG' 
ACCESS_TOKEN = '1105441700-aKxXANu5r3KZ4SYB28OpYfEpqip9nSqnnpA51Qs' 
ACCESS_TOKEN_SECRET = 'DNw53zlBrdc4Jf7gJLFLAzurYSSVZoBrGdsQXtZ0fNC7S' 

from twitter import Twitter, OAuth
#import pprint

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)

twitter = Twitter(auth = twitter_oauth)
#results = twitter.search.tweets(q='kapil sharma')
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(results)

def get_tweets(query):
    tweets = twitter.search.tweets(q="#" + query)
    return tweets                               
                                 

def get_num_followers(query):
    #import json
    #import sys
    num_followers = 0
    tweets = get_tweets(query)
    #print (tweets)
    #with open('file123.txt', 'w') as f:
     #   print(json.dumps(tweets), file=f)
    #print(json.dumps(tweets))
    for each_tweet in tweets['statuses']:
        print(each_tweet['user']['followers_count'])
        num_followers+=each_tweet['user']['followers_count']
    return num_followers

def main():
    while(True):
        user_choice = input("1. Count the Followers of Peope Tweeting using a certain hash tag.\n"
                            "2. Determine the Location, Timezone and language of people tweeting using a certain hash tag.\n"
                            "3. Number of times Modi has refered to US in the past 200 tweets compared to how many times Trump has mentioned India.\n"
                            "4. Determine the Sentiment of People Tweeting using a certain hash tag.\n"
                            "5. Top used words by PM Modi on Twitter.\n"
                            "6. Tweet a message from your account.\n"
                            "7. Exit\n")
        if user_choice == '1':
            user_input = input("Enter the Hash tag:")
            print("\n\n Max. number of users who have seen this hash tag: %s"% (get_num_followers(user_input)))
            
        elif user_choice == '2':
            #user_input = raw_input("Enter the Hash tag: ")
            #demographic_data(user_input)
            pass
        elif user_choice == '3':
            #ModiVsTrump()
            pass
        elif user_choice == '4':
            #user_input = raw_input("Enter the Hash tag")
            #sentiment_analysis(user_input)
            pass
        elif user_choice == '5':
            #ModiTopWords()
            pass
        elif user_choice == '6':
            #user_input = raw_input("Enter the Tweet: ")
            #add_tweet(user_input)
            pass
        elif user_choice == '7':
            break
        
        else:
            print("I did'nt get that. Please try again...\n")
        
        
main()

    