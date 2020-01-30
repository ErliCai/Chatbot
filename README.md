# This is a chatbot that helps you to :
 1 Get inforrmation of an artist   
 2 Get songs from an artist   
 3 Help you to find similar artist

## demo

![](demo/demo.gif)

<br>

# configuration  
This chatbot is built using rasa_nlu, SQLite, spacy and genius API from rapidAPI   
## spaCy  
```
conda install -c conda-forge spacy=2.0.11  
python -m spacy download en_core_web_md
```
## rasa_nlu
```
pip install rasa-nlu=0.13.7
```
Currently, the lastest version of rasa-nlu is 0.15.1, but it is not compatible with python 3.6

## Genius API

Genius API doesn't need to install. Could simply go on their webpage and request an access.   
Link is  https://rapidapi.com/brianiswu/api/genius
## wxpy

wxpy support Python 3.4-3.6, and 2.7 version<br>

```
pip install -U wxpy
```

***For more installation information***<br>
Go to https://wxpy.readthedocs.io/zh/latest/#<br>



 This chatbot is built using rasa_nlu, SQLite, spacy and genius API from rapidAPI  
 rasa_nlu helps with training data and, together with regular expression, extract intent of a sentence  
 SQLite helps with creating a database and search for artist match for the parameters (County and Genre)  
 spacy helps with finding entities  
 genius API provide easy access to datas like artist's besk known songs, lyrics of each song, artist activities.
