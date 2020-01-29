#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:55:40 2020

@author: cai
"""

import re


message = 'Jay Chou is a popular Taiwanese musician, one of the “big four” of Taiwanese pop whose fame is quite possibly unparalleled. '


def Get_Info(message):
    keywords = {
                'Country': ['Taiwan', 'British','Australia','American','Chin'], 
                'Genre': ['pop', 'rap','rock','jazz'], 
                }
    # Define a dictionary of patterns
    patterns = {}

    # Iterate over the keywords dictionary
    for intent, values in keywords.items():
        # Create regular expressions and compile them into pattern objects
        patterns[intent] = re.compile("|".join(values))

    
    Country = re.search(patterns['Country'],message)
    Country = Country.group(0)
    
    
    Genre = re.search(patterns['Genre'],message)
    Genre = Genre.group(0)
    
    return Country , Genre

    
    
#(Country , Genre ) = Get_Info(message) 
#print(Country)
