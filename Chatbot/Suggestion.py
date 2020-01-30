#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:44:42 2020

@author: cai
"""
#Sugget an artist base on local database

import sqlite3
from FindArtistInfo import Get_Artist_Info
from GetGenre import Get_Info

#Artis_Name = 'Jay Chou'

def Giving_Suggestion(Artist_Name):
    conn = sqlite3.connect('artist.db')

    # Create a cursor
    c = conn.cursor()

    # Define area and price
    Description =  Get_Artist_Info(Artist_Name)
    (Country, Genre) = Get_Info(Description)
    t = (Country, Genre)

    # Execute the query
    c.execute('SELECT * FROM artist WHERE Country=? AND Genre=?', t)
    
    return c.fetchall()
    
#print(Giving_Suggestion('Jay Chou'))
    
