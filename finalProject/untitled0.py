#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:45:35 2018

@author: samibialozynski
"""

import tweepy
import time
from codes import * 
from trainer import *

lat = float(39.2189)
long = float(-76.0690)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)

trends = api.trends_place(2358820)
data = trends[0]
getTrends = data['trends']
names = [trend['name'] for trend in getTrends]

allTrends = []

for x in names: 
    allTrends.append(x)


lastresponse = ""
count = 0
while True:
    
    
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    tweet = api.user_timeline(id = '983813133075656704', count = 1)[0]
    
    response = chatbot.get_response(tweet.text)
    if response != lastresponse:
        api.update_status(response)
        lastresponse = response
    else:
        api.update_status(allTrends[count] + "?")
        count += 1
 
        
    time.sleep(15)


