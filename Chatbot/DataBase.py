#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:12:34 2020

@author: cai
"""

#creat a database of artist using SQLite


import sqlite3
conn = sqlite3.connect('artist.db')
c = conn.cursor()
c.execute("DROP TABLE artist")
c.execute("CREATE TABLE IF NOT EXISTS artist(name text, Country,Genre)")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Eminem','American','rap')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('JJ Lin', 'Taiwan', 'pop')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Jolin Tsai', 'Taiwan', 'pop')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Li Ronghao', 'Chin', 'pop')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Jony J', 'Chin', 'rap')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Adele', 'British', 'pop')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Mayday', 'Taiwan', 'rock')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Greenday', 'American', 'rock')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Queen', 'British', 'rock')")
c.execute("INSERT INTO artist(name, Country, Genre) VALUES('Stormzy', 'British', 'rap')")
c.execute("commit")
