import re
import nltk
from nltk import word_tokenize
from bs4 import BeautifulSoup
import urllib
from urllib import request
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import wordnet

source=urllib.request.urlopen("https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison").read().decode("utf-8")
soup=BeautifulSoup(source,'html5lib')

Text = ''
for para in soup.find_all('p'):
    Text +=(para.text)#Original Text

print(Text) #DISPLAY ORIGINAL TEXT EXTRACT FROM URL 
lowertext=Text.lower() # convert MAIN TEXT  into lower

# remove punctuation  Before LOWERING 
mytext_tokens_nopunct = [word for word in word_tokenize(Text)
if re.search("\w", word)]

#Removing Punctuation After LOWRING
mylowertext_tokens_nopunct = [word for word in word_tokenize(lowertext)
if re.search("\w", word)]


print('TYPES BEFORE LOWERING AND LEMMATIZER  ')
print(len(set(mytext_tokens_nopunct)))
print('tokens BEFORE LOWER AND LEMMATIZER ')
print(len(mytext_tokens_nopunct))
print('TYPES AFTER LOWER  ')
print(len(set(mylowertext_tokens_nopunct)))
print('tokens AFTER ')
print(len(mylowertext_tokens_nopunct))

#NOW LAMMATIZING
wordnet_lemmatizer = WordNetLemmatizer()
nltk_tokens = nltk.word_tokenize(lowertext)
mylemma_tokens_nopunct = [word for word in word_tokenize(lowertext)
if re.search("\w", word)]
w1=[]
for w in nltk_tokens:
    w1.append(wordnet_lemmatizer.lemmatize(w))
#print ((w1))
print('TYPES AFTER  LEMMATIZER  ')
print(len(set(mylemma_tokens_nopunct)))
print('TOKENS AFTER  LEMMATIZER ')
print(len(mylemma_tokens_nopunct))

