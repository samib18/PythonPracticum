#Chat Twitter Bots
#I have one half of a chate twitter bot that will go through a conversation of things
#The code checks to make sure that statuses are not repeated because using the tweepy library you cannot duplicate statuses
#If there is a duplication error the bot will tweet about the current trends in Baltimore, MD area
import tweepy
import time
from codes import * 
from trainer import *

lat = float(39.2189)
long = float(-76.0690)


#The codes given from my specific twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Getting the trends for Baltimore, MD
trends = api.trends_place(2358820)
data = trends[0]
getTrends = data['trends']
names = [trend['name'] for trend in getTrends]

allTrends = []

#Placing the trends in a list so they can be tweeted
for x in names: 
    allTrends.append(x)
 
message = ""
print("go into loop")
notDuplicated = True
count = 0
while 1:
    
    
#tweet = api.user_timeline(id = '983813133075656704', count = 1)[0]
    if notDuplicated == True:
        print("It's not duplicated")
        #The id of the other Twitter bot user
        tweet = api.user_timeline(id = '983813133075656704', count = 1)[0]
        print(tweet.text)
        #Set up for a message
        message = chatbot.get_response(tweet.text)
        
    else:
        #If duplicated set message to a trend
        message = allTrends[count]
        count += 1
        notDuplicated = True    
   
    try:
        #Set the status based on message
        api.update_status(message)
        
    except tweepy.TweepError:
            print("Duplicated")
            notDuplicated = False
            
        

    #Tweet every 40 seconds
    time.sleep(40)
    print("one loop end")



