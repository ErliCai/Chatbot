#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:09:22 2020

@author: cai
"""

#connect to Genius API to get the name of song from an artist

import json
import requests


def Find_A_Song(name):
    url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":name}

    headers = {
    'x-rapidapi-host': "genius.p.rapidapi.com",
    'x-rapidapi-key': "3998edbee2mshe1989a5e18deb63p1ba0ecjsnf84da85afb0f"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    d = json.loads(response.text)
    
    name1 = d['response']['hits'][0]['result']['primary_artist']['id']
    name2 = d['response']['hits'][1]['result']['primary_artist']['id']
    
    if name1 != name2:
        response = 'There are multiple artist with name {0} \nPlease give me a more specific name'
        response = response.format(name)
        print(response)
        return [123 , response]
    else:
        artist_id = name1
        song_name = d['response']['hits'][0]['result']['title']
        
        return  [artist_id  ,  song_name]

#print(Find_A_Song('Jay Chou'))
