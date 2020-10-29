import nltk
import re

text =(" so I need to match  +55 51 33083838, 1206 872020,01206 872020 ,05679401945 , +44 5679401945 , 0044 5679401945 Can y" )
print('Found a  matchs')
print('Telephones:')
phone_regex = re.compile("([\+|0|1])\s*(\d{1,10})\s*(\d{1,})\s*(\d{1,})")
groups = phone_regex.findall(text)
i=1
for g in groups:
    print("".join(g))
    i+=1



