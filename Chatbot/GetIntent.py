#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:17:21 2020

@author: cai
"""

#Combine EasyIntent and ComplexIntent
# Search for Easy Intent first because it;s quicker. If find anything we could skip uising ComplexIntent

from EasyIntent import easy_intent
from ComplexIntent import complex_intent


#sentence =  "I don't like him"

def Get_Intent(message):
    
    if easy_intent(message) != None:
        return easy_intent(message)
    else:
        intent = complex_intent(message)
    return intent['name']
        
    
#print(Get_Intent(sentence)) 
