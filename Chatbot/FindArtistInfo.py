#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:26:53 2020

@author: cai
"""

import json
import requests
from FindASong import Find_A_Song


def Get_Artist_Info(artist_name):
    
    (artist_id,song_name) = Find_A_Song(artist_name)

    url = "https://genius.p.rapidapi.com/artists/"
    url = url + str(artist_id)
    
    headers = {
            'x-rapidapi-host': "genius.p.rapidapi.com",
            'x-rapidapi-key': "3998edbee2mshe1989a5e18deb63p1ba0ecjsnf84da85afb0f"
            }

    response = requests.request("GET", url, headers=headers)

    d = json.loads(response.text)
    artist_info = d['response']['artist']['description']['dom']['children'][0]['children']

    sentences =  []
    for information in artist_info:
        if isinstance(information, str):
            sentences.append(information)
        else:
            sentences.append(information['children'][0])
    sentence = ''.join(sentences)

    return sentence
    
#print(Get_Artist_Info('Jay Chou'))
#print(Get_Artist_Info(30874))
