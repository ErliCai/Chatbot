#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:37:27 2020

@author: cai
"""
# Respond to easy intent. This requires only one parameter(intent)

import random

def Easy_Respond(intent):
    
    
     if intent == 'greet':
        sentence = ['Hello',
                    "It's good to see you",
                    'Hi Buddy'
                ]
        message =  '{} \nWhat can I do for you today'
        message = message.format(random.choice(sentence))
     if intent == 'thankyou':
         message = 'You are welcome'
         
     if intent ==  'goodbye':
         sentence = ['Goodbye','Hope to see you next time']
         message = random.choice(sentence)
         
     if intent ==  'function':
         message = "I'm a chatbot\nI can help you to find songs from any artist\nAnd get a link to the lyrics\nOr to get information of any artist \nOr find similar artist"
         
     return message
 
 
