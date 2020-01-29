#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:04:27 2020

@author: cai
"""

import re
keywords = {
            'greet': ['hello', 'hey','Good Morning','Good Afternoon'], 
            'thankyou': ['thank', 'thx'], 
            'goodbye': ['bye', 'farewell','Good night'],
            'Negate': [ "don't" , "not" ]
           }
# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, values in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile("|".join(values))
#print(patterns)
    
def easy_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if re.search(pattern,message):
            matched_intent = intent
    return matched_intent