#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:28:20 2020

@author: cai
"""

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Create a trainer that uses this config
trainer = Trainer(config.load("config_spacy.yml"))

# Load the training data
training_data = load_data('rasa1.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

#messaage = 'tell me more about Sia'

def complex_intent(message):
    intent = interpreter.parse(message)["intent"]
    return intent

#intent = complexintent(messaage)
#print(intent)