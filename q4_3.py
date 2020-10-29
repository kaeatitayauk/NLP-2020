#1908054
import re
import os.path
from nltk.corpus import wordnet as wn
from itertools import product


def read_txt(file_path):  # read file splitting each text by spacing and store in dummy list
    with open(file_path, "r") as file:
        return [re.split("\s+", line.rstrip('\n')) for line in file]


list_text = (read_txt("original-pairs.txt"))  # feed file path to function above
del list_text[0]  # filter header out
w1_q, w2_q = [], []
dummy_words, hynp1, hynp2, dummy_hypn1, dummy_hypn2, list_similarity = [], [], [], [], [], []

for index in list_text:
    w1_q.append(index[0])
    w2_q.append(index[1])
    dummy_words.append(index[2])

index = 0
for hypn_searching in w1_q:  # loop to get the nearest hypernym of each word sense
    hynp1 = wn.synsets(w1_q[index])
    hynp2 = wn.synsets(w2_q[index])
    if hynp1:
        hynp1 = hynp1[0].hypernyms()
        if hynp1:
            hynp1 = hynp1[0].lemma_names()
            dummy_hypn1.append(hynp1[0])
    if hynp2:
        hynp2 = hynp2[0].hypernyms()
        if hynp2:
            hynp2 = hynp2[0].lemma_names()
            dummy_hypn2.append(hynp2[0])
    if not hynp1:
        dummy_hypn1.append("0.00")  # keep 0.00 when there's no hypernym for the word
    if not hynp2:
        dummy_hypn2.append("0.00")  # keep 0.00 when there's no hypernym for the word
    index += 1

index_w2 = 0
for index_w1 in dummy_hypn1:  # cross loop to check sense of the words and keep the top path similarity of individual word
    w1 = [index_w1]
    w2 = [dummy_hypn2[index_w2]]
    if w1 != ["0.00"] and w2 != ["0.00"]:
        list_w1 = set(w for word in w1 for w in wn.synsets(word))
        list_w2 = set(w for word in w2 for w in wn.synsets(word))
        if list_w1 and list_w2:
            max_similarity = max((wn.path_similarity(w1, w2) or 0.00, w1, w2) for w1, w2 in product(list_w1, list_w2))
            list_similarity.append(max_similarity[0])
    else:
        list_similarity.append('None')
    index_w2 += 1

pointer = 0
keeper = "word1\tword2\tSimilarity1\thyp1\thyp2\tSimilarity2\n"  # HEADING
for index in list_similarity:  # loop to join string
    keeper += (w1_q[pointer])
    keeper += "\t"
    keeper += (w2_q[pointer])
    keeper += "\t"
    keeper += (dummy_words[pointer])
    keeper += "\t"
    keeper += (dummy_hypn1[pointer])
    keeper += "\t"
    keeper += (dummy_hypn2[pointer])
    keeper += "\t"
    if not index:
        keeper += 'None'
    else:
        keeper += str(index)
    keeper += "\n"
    pointer += 1

save_path = 'original-pairs-hypernyms.txt'
if os.path.exists(save_path):
    update_file = open(save_path, 'w')
else:
    update_file = open(save_path, 'x')
    update_file = open(save_path, 'w')
update_file.write(keeper)
print(keeper)  # display out
