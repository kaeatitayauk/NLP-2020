#1908054
import re
import os.path

from nltk.corpus import wordnet as wn
from itertools import product


def read_txt(path):  # read file splitting each text by spacing and store in dummy list
    with open(path, "r") as file:
        return [re.split("\s+", line.rstrip('\n')) for line in file]


list_text = (read_txt('SimLex999-100.txt'))
del list_text[0]  # delete the header
origin_w1, origin_w2 = [], []
gold_similarity, list_similarity = [], []

for index in list_text:  # store words with the human similarity score in list
    origin_w1.append(index[0])
    origin_w2.append(index[1])
    gold_similarity.append(index[2])

index_w2 = 0
for index_w1 in origin_w1:  # loop to check the senses of words and cross check the path similarity to get the maximum ones
    w1 = [index_w1]
    w2 = [origin_w2[index_w2]]
    list_w1 = set(ss for word in w1 for ss in wn.synsets(word))
    list_w2 = set(ss for word in w2 for ss in wn.synsets(word))
    if list_w1 and list_w2:
        max_similarity = max((wn.path_similarity(w1, w2) or 0.00, w1, w2) for w1, w2 in product(list_w1, list_w2))
        list_similarity.append(max_similarity[0])
    index_w2 += 1

wds_pointer = 0
keepper = "word1\tword2\tGoldSimilarity\tWordNetSimiliarity\n"  # HEADING
for index in list_similarity:  # loop to keep all string from each member in list
    keepper += (origin_w1[wds_pointer])
    keepper += "\t"
    keepper += (origin_w2[wds_pointer])
    keepper += "\t"
    keepper += (gold_similarity[wds_pointer])
    keepper += "\t"
    keepper += str(index)  # turn index into string format
    keepper += "\n"
    wds_pointer += 1

update_path = 'BioSim-100-predicted.txt'

if os.path.exists(update_path):  # if file exists this cond just update the file
    update_file = open(update_path, 'w')
else:
    update_file = open(update_path, 'x')  # if not just create and write into
    update_file = open(update_path, 'w')
update_file.write(keepper)  # write into file
print(keepper)  # display to screen
