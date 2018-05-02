import tweepy
import time
from codes import * 
from trainer import *

lat = float(39.2189)
long = float(-76.0690)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

trends = api.trends_place(2358820)
data = trends[0]
getTrends = data['trends']
names = [trend['name'] for trend in getTrends]

allTrends = []

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
        tweet = api.user_timeline(id = '983813133075656704', count = 1)[0]
        print(tweet.text)
        message = chatbot.get_response(tweet.text)
        
    else:
        message = allTrends[count]
        count += 1
        notDuplicated = True
        
    
   
    try:
        api.update_status(message)
    except tweepy.TweepError:
            print("Duplicated")
            notDuplicated = False
            
        

    time.sleep(40)
    print("one loop end")



