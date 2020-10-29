#1908054
import os.path
import re
import operator
import random



def read_txt(file_path):
    with open(file_path, "r") as file:
        return [re.split("\s+", line.rstrip('\n')) for line in file]


list_txt = (read_txt('original-pairs.txt'))  # feed file path to function above
del list_txt[0]  # filter header out
# |1| UNCOMMENT LINE BELOW TO SEE VARIETY OF TOP SCORE |1|
# list_txt = random.sample(list_txt, len(list_txt))  # turn this if needing text in the list to be shuffled before hand
indexer = []

for i in list_txt:  # keep only read similarity score
    score = float(i[2])
    indexer.append([score])

index_of_inds = []
c = 0
while c < 10:  # loop 10 times to get top 10 of score as example (sorting)
    # actually there are more than 10 same similarity score in this task.
    # Change the number of looping above to get more information. Or use the shuffle by uncomment above commented |1|
    sorted = (max(enumerate(indexer),
                  key=operator.itemgetter(1)))  # get index of list and keep top similarity
    dummy_digit = sorted[0]
    index_of_inds.append(dummy_digit)
    indexer[index_of_inds[c]] = [0]
    c += 1

keeper = "word1\tword2\tSimilarity\n"  # HEADING
c = 0
for i in index_of_inds:  # loop to keep in string format
    top_index = index_of_inds[c]
    wds = '\t'.join(list_txt[top_index])
    keeper += wds
    keeper += "\n"
    c += 1

save_path = 'top.txt'
if os.path.exists(save_path):
    update_file = open(save_path, 'w')
else:
    update_file = open(save_path, 'x')
    update_file = open(save_path, 'w')
update_file.write(keeper)
print(keeper) # display out
