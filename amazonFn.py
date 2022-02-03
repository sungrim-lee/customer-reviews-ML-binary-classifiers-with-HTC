#!/usr/bin/env python
# coding: utf-8

# Load libraries needed
from bs4 import BeautifulSoup       
import unicodedata                  
import contractions                 
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re                           
from nltk.stem import PorterStemmer 


# remove tags
def removeTags(text):
    return BeautifulSoup(text, 'html.parser').get_text()

# remove accents
def removeAccents(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

# append contracted text
def appendContractions(text):
    appendedWords = []
    for word in text.split():
        appendedWords.append(contractions.fix(word))
    return ' '.join(appendedWords)

# remove stopwords
exceptStopwords = []
# ENGLISH_STOP_WORDS.difference(['not'])
def removeStopwords(text):
    words = [word for word in text.split() if word.lower() not in ENGLISH_STOP_WORDS]
    return " ".join(words)

# remove white spaces
def removeWhitespaces(text):
    return re.sub(r'^\s*|\s\s*', ' ', text).strip()

# lemmatize words
def lemmatizeWords(text):
    ps = PorterStemmer()
    return ' '.join([ps.stem(word) for word in text.split()])

