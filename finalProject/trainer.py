#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:11:01 2018

@author: samibialozynski
"""
from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

#chatbot.train("chatterbot.corpus.english")

#chatbot.train("chatterbot.corpus.english.greetings")

#chatbot.train("chatterbot.corpus.english.conversations")