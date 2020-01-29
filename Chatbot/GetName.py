#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:57:57 2020

@author: cai
"""

import spacy
import numpy as np


nlp = spacy.load('en_core_web_md')
include_entities = ['PERSON']

# Define extract_entities()
def extract_name(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents['PERSON']

#print(extract_entities('friends called Mary who have worked at Google since 2010'))
#print(extract_name('Jay Chou'))