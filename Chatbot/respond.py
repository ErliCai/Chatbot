#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:02:33 2020

@author: cai
"""
import random
from EasyRespond import Easy_Respond
from FindASong import Find_A_Song
from FindArtistInfo import Get_Artist_Info
from Suggestion import Giving_Suggestion
from GetIntent import Get_Intent
from GetName import extract_name


#message = 'Tell me more about Jay Chou'        
#message = "I don't like him"

def Respond( message , lastintent = None , lastartist = None ):
    
    intent = Get_Intent(message)    
    artist = extract_name (message)
    
    if artist == None:
        artist = lastartist
    
    print(intent)
    print(lastintent)

    AskingForArtist = ['Which Artist are you looking for?',
            'Sorry, which Artist are we talking about?',
            'I think you forget to mention which artist you are looking for'
            ]
    if intent == 'greet' or intent == 'thankyou' or intent == 'goodbye' or intent == "function":
        message = Easy_Respond(intent)
        
    elif intent == "find a song":
            if artist != None:
                message = Find_A_Song(artist)[1]
            else:
                    message = random.choice(AskingForArtist)
                    
    elif intent == "Artist Information":
        if artist != None:
            message = Get_Artist_Info(artist)
        else:
            message = random.choice(AskingForArtist)   
                   
    elif intent == "find similar":
        if artist != None:
            message = Giving_Suggestion(artist)[0][0]
        else:
            message = random.choice(AskingForArtist)

    if intent == 'Negate':
        message = Giving_Suggestion(artist)[1][0]
        print(message)
        
    return message , intent, artist 
        

#(reply, lastintent, lastartist)  =  Respond(message)
#print(reply)   

        
        
        
        
        
        