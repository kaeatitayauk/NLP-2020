import re
import nltk
#from nltk import pos
from nltk import word_tokenize
from bs4 import BeautifulSoup
import urllib
from urllib import request

from nltk import wordnet

source=urllib.request.urlopen("https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison").read().decode("utf-8")
soup=BeautifulSoup(source,'html5lib')

Text = ''
for para in soup.find_all('p'):
    Text +=(para.text)#Original Text
print(Text)
tokenized = nltk.word_tokenize(Text)
print(nltk.pos_tag(tokenized,'universal'))
