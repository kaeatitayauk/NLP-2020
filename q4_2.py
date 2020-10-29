#1908054
from nltk.corpus import wordnet as wn
from itertools import product
from nltk.tokenize import RegexpTokenizer
import nltk.data
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import os.path


def read_txt(path):  # read file splitting each text
    with open(path, "r") as file:
        return file.read()


list_text = (read_txt('text1.txt'))
list_text = list_text.lower()  # lower text to not consider the capital letters
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
lemmatizer = WordNetLemmatizer()

cleanner = " ".join([lemmatizer.lemmatize(i) for i in list_text.split()])  # lemma to reduce tokens of the text

pointer, cond = 0, 0
cleanner = (cleanner.split())
for loop1 in cleanner:  # loop to join text from the splitter
    if cond == 0:
        for loop_cond in cleanner:
            cleanner[pointer] = cleanner[pointer].replace('--', " ")
            pointer += 1
    pointer = 0
    if cond == 1:
        for loop_cond in cleanner:
            cleanner[pointer] = cleanner[pointer].replace('-', "")
            pointer += 1
    pointer = 0
    if cond == 2:
        for loop_cond in cleanner:
            cleanner[pointer] = cleanner[pointer].replace('_', " ")
            pointer += 1
    cond += 1

cleanner = ' '.join(cleanner)
tokenizer = RegexpTokenizer(r'\w+')
list_word = []
cleanner = tokenizer.tokenize(cleanner)
cleanner = list(dict.fromkeys(cleanner))
cleanner = [word for word in cleanner if word not in stopwords.words('english')]  # apply stopwords remover
index_del = 0
for pointer in cleanner:
    if len(pointer) == 1:
        cleanner.remove(pointer)
    if pointer == "wa" or pointer == "wer" or pointer == "ha":  # remove common mistake stopwords after stemming
        del cleanner[index_del]
    index_del += 1

for pointer in cleanner:
    list_word.append(tokenizer.tokenize(pointer))

score = []
token_w1, token_w2 = [], []

for pointer in list_word:
    token_w1.append(pointer)
    token_w2.append(pointer)

w1_list, w2_list = [], []
token_w1 = [item for sublist in token_w1 for item in sublist]
token_w2 = [item for sublist in token_w2 for item in sublist]

for word1n in token_w1:  # cross loop to check sense of the words and keep the top similarity of individual word
    for word2n in token_w2:
        if word1n != word2n:
            w1_list.append(word1n)
            w2_list.append(word2n)
            w1 = [word1n]
            w2 = [word2n]
            temp_w1 = set(w for word in w1 for w in wn.synsets(word))  # store the senses of 1 into dummy list
            temp_w2 = set(w for word in w2 for w in wn.synsets(word))  # store the senses of 2 into dummy list
            if temp_w1 and temp_w2:
                top_similar = max(
                    (wn.path_similarity(w1, w2) or 0.00, w1, w2) for w1, w2 in product(temp_w1, temp_w2))
                score.append(top_similar[0])
            else:
                score.append(0.0)

detect = "word1\tword2\tSimilarity\n"  # HEADING
wds_pointer = 0
for pointer in score:  # loop to join string
    detect += (w1_list[wds_pointer])
    detect += "\t"
    detect += (w2_list[wds_pointer])
    detect += "\t"
    detect += str(pointer)
    detect += "\n"
    wds_pointer += 1

save_path = 'original-pairs.txt'
if os.path.exists(save_path):
    update_file = open(save_path, 'w')
else:
    update_file = open(save_path, 'x')
    update_file = open(save_path, 'w')
update_file.write(detect)
print(detect)
