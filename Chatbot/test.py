#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:46:23 2020

@author: cai

"""

import random

intent = "greet"

if intent == 'greet':
        sentence = ['Hello',
                    "It's good to see you",
                    'Hi Buddy'
                ]
        message = random.choice(sentence) + ' \nWhat can I do for you today'
        
print(message)


      