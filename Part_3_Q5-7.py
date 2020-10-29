import nltk #import nltk package
import collections # import collections package
from collections import Counter, defaultdict # import counter and defaultdict to count the number of occurrences
import re # import regular expression package
from tabulate import tabulate #import package 'tabulate' to display table

# this function reads the files and split words by space (\s+) and define number of array by \n
def read_file(file_path):
    with open(file_path) as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

# this function needs 2 parameters from read file ## to remove <s> and </s> from the data set
def remove_cover(text, cond):
    if cond == "model": #do if cond given = "model"
        for a in (text):
            del a[0]
            del a[-1]
        remove_cover.data = []
        for a in (text):
            remove_cover.data += a
    if cond == "prob":#do if cond given = "prob"
        for a in (text):
            del a[0]
            del a[-1]

# this function is used to calculate UNIGRAM probability of each word and UNK ## 2 parameters are used in this function 1) data set without <s>,</s> 2) number of UNK found
def unigram_model(data_set, unk):
    data_occurrence = collections.Counter(data_set) # 'data_occurrence' is stored number of occurrences of each word in data set
    data_index = list(data_occurrence) # 'data_index' stores list of 'data_occurrence'
    letter_count = 0 # define 'letter_count' to 0
    unigram_prob = [] # set 'unigram_prob' as list
    for values in data_occurrence: # loop 'data_occurrence' to keep values of 'data_occurrence' and count number of letters in the data set
        letter_count += data_occurrence[values]
    i = 0 # set 'i' = 0 and is used to point the index of 'data_index'
    for c in data_occurrence: # loop 'data_occurrence' to add values into 'unigram_prob'
        unigram_prob.append((data_index[i], round((data_occurrence[c] / letter_count), 5))) # using append to add value to 'unigram_prob' and calculate unigram probability
        # using unigram formula == (word occurrence) / number of words in data set
        i += 1
    unigram_prob.append(("UNK", round((unk / (letter_count + unk)), 5))) # using append to add value to 'unigram_prob' and calculate unigram probability of UNK
    print(tabulate(unigram_prob, headers=['Word', 'Probability'], tablefmt='orgtbl')) #display unigram probability in table

# this function is used to calculate UNIGRAM Laplace smoothing probability of each word and UNK
def unigram_model_laplace(data_set, unk, vocab, uncover_sentence, is_sentence): #and also calculate UNIGRAM sentence probability
    #  5 parameters are using in this function 1)data set without <s>,</s> 2)number of UNK found  3)number of vocabulary 4)sentence data set 5)condition for calculate unigram sentence probability
    data_occurrence = collections.Counter(data_set) # 'data_occurrence' is stored number of occurrences of each word in data set
    data_index = list(data_occurrence) # 'data_index' stores list of 'data_occurrence'
    letter_count = 0 # define 'letter_count' to 0
    unigram_laplace_prob = [] # set 'unigram_laplace_prob' as list
    for values in data_occurrence:   # loop 'data_occurrence' to keep values of 'data_occurrence' and count number of letters in the data set
        letter_count += data_occurrence[values]
    i = 0 # set 'i' = 0 and is used to point the index of 'data_index'
    if is_sentence != "true": # do if this function is called with 'is_sentence' not equal to "true"
        for c in data_occurrence: # loop 'data_occurrence' to add values into 'unigram_laplace_prob'
            unigram_laplace_prob.append((data_index[i], round((data_occurrence[c] + 1) / (vocab + letter_count + 1), 5))) # UNIGRAM LAPLACE smoothing formula is used here
            #(word ocurrence +1) / (number of vocabulary + number of words +1 )
            i += 1
    if is_sentence != "true": # do if this function is called with 'is_sentence' not equal to "true"
        unigram_laplace_prob.append(("UNK", round(((unk + 1) / (vocab + letter_count + unk + 1)), 5))) # using append to add value to 'unigram_laplace_prob' and calculate unigram probability of UNK
        print(tabulate(unigram_laplace_prob, headers=['Word', 'Probability'], tablefmt='orgtbl')) #display unigram smoothing probability in table

    sentence_prob = [[]] * i # define 'sentence_prob' as list of list * i to store values of each word probability
    i = 0
    if is_sentence == "true":  # do if this function is called with 'is_sentence' equal to "true" (calculate sentence probability)
        unk -= 1
        for c in data_occurrence:
            sentence_prob.append([data_index[i], round((data_occurrence[c] + 1) / (vocab + letter_count + 1), 5)]) # used the same UNIGRAM LAPLACE calculation above to store each word probability in 'sentence_prob'
            i += 1
        one_d_array = [item for sublist in sampledata_vocab for item in sublist] # turn sampledata_vocab in to 1D array as 'one_d_array'
        vocab_set = set(one_d_array) # set 'vocab_set' as set of values in 'one_d_array'
        sentence_set = set(uncover_sentence) # set 'sentence_set' as set of values in 'uncover_sentence' (sentence data set)
        sentence_unk = sentence_set.intersection(vocab_set) # intersection each of above set to get UNK in sentence data set
        my_list = list(sentence_unk) # define 'my_list' as list of 'sentence_unk'
        j = len(sentence_prob) # define 'j' as number of length of sentence_prob
        unigram_model_laplace.num = 0 # 'unigram_model_laplace.num' = 0 (this parameter will be used to keep value of each sentence probability)
        sum = 0 # set sum = 0 to summation each of the word probability in a sentence
        count = 0 # set count = 0 to count number of loop and will use to check condition to pass value to 'sum'
        sentence_unk = (len(sentence_set)) - (len(sentence_unk)) # check if there is UNK in a sentence
        for i in my_list: # outer loop of 'my_list'
            for h in sentence_prob: #inner loop of item in 'sentence_prob'
                if (sentence_prob[j - 1][0]) == i:
                    sum = sentence_prob[j - 1][1] # add every value of word in sentence to 'sum'
                    count += 1 # now plus 1 to 'count'
                j -= 1 # decrease value of 'j'
                if count == 1:
                    unigram_model_laplace.num = sum # pass valuse of sum to  unigram_model_laplace.num
                if count > 1 and sentence_prob[j][0] == i:
                    unigram_model_laplace.num = round(unigram_model_laplace.num * sum, 5) # after 1st loop 'unigram_model_laplace.num' will start to calculate sentence probability by multiply every word probability together
            j = len(sentence_prob) # reset 'j'
        if sentence_unk >= 1: # if there is UNK in a sentence
            unigram_model_laplace.num = round(
                unigram_model_laplace.num * (((unk + 1) / (vocab + letter_count + unk + 1)) ** sentence_unk), 5) # unk probability will be add and calculate in to the sentence probability

# this function will check number of UNK in data set compare with vocab
def unk_count(vocab_lenght, data_uncover): # 2 parameters are used in this 1)vocab 2) dataset with no <s>, </s>
    unk_count.list = []  #  unk_count.list as list
    for a in sampledata_vocab: # loop to add every vocab into 'unk_count.list'
        if vocab_lenght >= 1:
            unk_count.list += a # adding vocab to list
    set_sample_data = set(data_uncover) # set 'set_sample_data' as a set of 'data_uncover'
    set_vocab_sample_data = set(unk_count.list) # set 'set_vocab_sample_data' as a set of 'unk_count.list'
    unk_count.unk = len(
        (set_sample_data.union(set_vocab_sample_data) - set_sample_data.intersection(set_vocab_sample_data))) # now check if we have UNK by union then - with data intersection vocab

# this function creates bigram pairs of data set
def into_bigram_pair(data):  # 1 parameter is used here is 'data' (original data set with <s>, </s>)
    data = [item for sublist in data for item in sublist] # loop to make item in data set into one list
    text = " ".join(data) # text = join every item in data using space to split
    into_bigram_pair.data = list(nltk.bigrams(text.split())) # this called nltk package to split words into pairs (bigram)
    index = len(into_bigram_pair.data) - 1 # set 'index' to length of into_bigram_pair.data to use for looping
    for item in into_bigram_pair.data: # loop to remove the pair that contains </s> as the first word in the pair
        if into_bigram_pair.data[index][0] == "</s>":
            del into_bigram_pair.data[index] # del that pair 'into_bigram_pair.data' at 'index' count
        index -= 1 # decrease index evertime of the loop

# this fucntion is use to calculate the probability of BIGRAM unsmoothing using dataset without cutting starting and ending sentence
def bigram_unsmoothed(data, bigram_data, unmatched_set): #and also uses bigram pairs of data set, and 'unmatched set' means the posible pairs that not occur in the bigramd data
    unmatched_set = collections.Counter(unmatched_set) #count the number of unmatched pair
    bigram_unsmoothed.ind = collections.Counter(data) # count the number of each word occured in the data set given
    bigram_unsmoothed.pair = collections.Counter(bigram_data) # count the number of pairs in the data set given
    bigram_list = list(bigram_unsmoothed.ind) # 1
    pair_values = list(bigram_unsmoothed.pair) # 2
    unknown_pair = list(unmatched_set) # 3 # from 1-3 turn the counting information above into lists
    i = 0
    j = len(bigram_list) # count the length of data set counting
    bigram_unsmoothed_prob = [] # define 'bigram_unsmoothed_prob' as a list
    for c in bigram_unsmoothed.pair: # outer loop = 'bigram_unsmoothed.pair' items
        for x in range(j): # inner loop = 'length of data set count'
            if i == len(pair_values):  # break before number of index in  'pair_values' exceeding the last index
                break
            if bigram_list[j - 1] == pair_values[i][0]: # do if finds word match with the first pair word
                x = (list(bigram_unsmoothed.ind.values())[j - 1]) # pass values of the number of pair into 'x'
                bigram_unsmoothed_prob.append((pair_values[i], round((bigram_unsmoothed.pair[c]) / (x), 5))) # use the bigram formula to calculate the prob. of each pair and add the value into 'bigram_unsmoothed_prob'
                ## along with the particular pair data
                i += 1
            j -= 1
        j = len(bigram_list) # reset the length of j to loop again until the outer loop ends
    j = len(bigram_list) # again set j equal to length of counted data set
    i = 0
    for c in unmatched_set: # this loop will do the same way of the above loop but use the not occur pair in the bigram of data set
        for x in range(len(bigram_list)):
            if i == len(unknown_pair):
                break
            elif bigram_list[j - 1] == unknown_pair[i][0]:
                bigram_unsmoothed_prob.append((unknown_pair[i], 0)) # we don't need formula here because this always 0 (not like add-one smoothing that can have values)
                i += 1
            j -= 1
        j = len(bigram_list)
    i = 0
    j = len(bigram_list)
    for c in bigram_unsmoothed.pair: # this loop used to calculate the prob. of pair that has UNK or UNK and UNK in the pair
        if i == j:
            break # use break before counting of 'i' exceed the last index in the list in 'bigram_list'
        num = (list(bigram_unsmoothed.ind.values())[i]) # store value of counted pair in data set
        bigram_unsmoothed_prob.append(((bigram_list[i], 'UNK'), round(unk_count.unk / (num + len(bigram_list)), 5))) # now add the values of calculation into 'bigram_unsmoothed_prob' list to use later
        bigram_unsmoothed_prob.append((("UNK", bigram_list[i]), round(unk_count.unk / len(bigram_list), 5)))  # now add the values of calculation into 'bigram_unsmoothed_prob' list to use later
        i += 1
    bigram_unsmoothed_prob.append((("UNK", "UNK"), unk_count.unk / len(bigram_list))) # calculate prob. of UNK and UNK in the same pair and add into 'bigram_unsmoothed_prob'
    print(tabulate(bigram_unsmoothed_prob, headers=['Pairs occurrence', 'Probability'], tablefmt='orgtbl')) # display all of the prob. in table


# this function does the same method of function 'bigram_unsmoothed' but use the LAPLACE smoothing formula to calculate the prob. of bigram
def bigram_smoothed_laplace(data, bigram_data, unmatched_set): # use the same parameters as 'bigram_unsmoothed' uses
    unknown_pair = list(unmatched_set)
    unk_count.unk += 1
    bigram_smoothed_laplace.ind = collections.Counter(data)
    list_data_count = list(bigram_smoothed_laplace.ind)
    bigram_smoothed_laplace.pair = collections.Counter(bigram_data)
    arr = list(bigram_smoothed_laplace.pair)
    i = 0
    j = len(list_data_count)
    bigram_smoothed_laplace.store_prob = []
    bigram_smoothed_laplace_prob = []
    for C in bigram_smoothed_laplace.pair:
        for x in range(len(list_data_count)):
            if i == len(arr):
                break
            if list_data_count[j - 1] == arr[i][0]:
                counted_data_letter = list(bigram_smoothed_laplace.ind.values())[j - 1]
                counted_pair = bigram_smoothed_laplace.pair[C]
                bigram_smoothed_laplace.store_prob.append([arr[i], ((((counted_pair + 1) / (
                        counted_data_letter + len(list_data_count)))))])
                bigram_smoothed_laplace_prob.append((arr[i], round(((counted_pair + 1) / (
                        counted_data_letter + len(list_data_count))), 5)))
                i += 1
            j -= 1
        j = len(list_data_count)

    i = 0
    k = 2
    for x in unknown_pair:
        if i == len(unknown_pair) or k < 0:
            break
        counted_data_letter = list(bigram_smoothed_laplace.ind.values())[k]
        bigram_smoothed_laplace.store_prob.append([unknown_pair[i], ((1 / ((counted_data_letter) + len(list_data_count))))])
        bigram_smoothed_laplace_prob.append((unknown_pair[i], round(1 / ((counted_data_letter) + len(list_data_count)), 5)))
        k -= 1
        i += 1
    i = 0
    for c in bigram_smoothed_laplace.pair:
        if i == j:
            break
        counted_data_letter = list(bigram_smoothed_laplace.ind.values())[i]
        bigram_smoothed_laplace.store_prob.append(
            [(list_data_count[i], 'UNK'), (unk_count.unk / (counted_data_letter + len(list_data_count)))])
        bigram_smoothed_laplace_prob.append(((list_data_count[i], 'UNK '), round((unk_count.unk / (counted_data_letter + len(list_data_count))), 5)))
        bigram_smoothed_laplace.store_prob.append([("UNK", list_data_count[i]), (unk_count.unk / len(list_data_count))])
        bigram_smoothed_laplace_prob.append((("UNK", list_data_count[i]), round(unk_count.unk / len(list_data_count), 5)))
        i += 1
    bigram_smoothed_laplace.store_prob.append([("UNK", "UNK"), (unk_count.unk / len(list_data_count))])
    bigram_smoothed_laplace_prob.append((("UNK", "UNK"), round(unk_count.unk / len(list_data_count), 5)))
    print(tabulate(bigram_smoothed_laplace_prob, headers=['Pairs occurrence', 'Probability'], tablefmt='orgtbl'))

# this function calculates sentence probability by multiplying each of bigram data in each sentence using values of bigram laplace smoothing we have stored
def bigram_sentence_probabality(data, text_bigram):
    bigram_sentence_probabality.prob = 0
    i = 0
    count = 0
    num = 0
    j = len(text_bigram)
    for c in data:
        for x in text_bigram:
            if text_bigram[j - 1][0] == data[i]:
                num = text_bigram[j - 1][1] # pass the value of 'text_bigram' to 'num'
                count += 1
            j -= 1
            if count == 1:
                bigram_sentence_probabality.prob = num # pass the value of num to 'bigram_sentence_probabality.prob'
            if count > 1 and text_bigram[j][0] == data[i]:
                bigram_sentence_probabality.prob = bigram_sentence_probabality.prob * num # now multiply them together
        i += 1
        j = len(text_bigram)

# this function calculates all of the possible pair in the BIGRAM
def all_possible_pair():
    all_possible_pair.store_all_pos = []
    flat = [item for sublist in sampledata_vocab for item in sublist] # makes the list of vocab list into just list of vocab
    flat.insert(0, "<s>") # add <s> at first index
    flat.append("</s>") # add </s> at the last index
    for c in flat: # loop at number of item in 'flat' (new vocab with <s>,</s>) by 'flat'
        for x in flat:
            all_possible_pair.store_all_pos.append((c, x)) # add all of the possible pair into 'store_all_pos'
    all_possible_pair.store_all_pos = list(all_possible_pair.store_all_pos)
    i = len(all_possible_pair.store_all_pos) - 1
    for a in all_possible_pair.store_all_pos: # now loop agian to remove </s> that occurs in the first word of pair
        if all_possible_pair.store_all_pos[i][0] == "</s>":
            del all_possible_pair.store_all_pos[i] # this is how I remove that item
            i = i - 1
    i = len(all_possible_pair.store_all_pos) - 1

    unwanted_pair = [('<s>', '<s>'), ('<s>', '</s>')] # set the pairs that we don't want in the bigram data
    y = 0
    for i in range(26): # loop 26 time (from a-z) to add the pair that we don't to calculate into 'unwanted_pair' means that a-z followed by starting sentence
        unwanted_pair.append((chr(ord('a') + y), '<s>'))
        y += 1
    set_unwanted = set(unwanted_pair) #1
    prm_first_set = set(all_possible_pair.store_all_pos) #2
    prm_second_set = set(into_bigram_pair.data) #4
    unmatched_set = prm_first_set - prm_second_set #5
    all_possible_pair.unmatched_set = unmatched_set - set_unwanted # now I extract and get only the pair that we don't have yet in the bigram data by substracting each set
    all_possible_pair.sampledata_cover = [item for sublist in read_sampledata_cover for item in sublist] # turn the 'read_sampledata_cover' (data set with <s>, </s>) into sampledata_cover as list

# this function will check the number of UNK in the sentence test given and change every word in the sentence that is UNK to UNK
def sort_list(sentence_data): # 1 parameter needs is sentence data
    sentence = [item for sublist in sentence_data for item in sublist] #1
    store_raw_vocab = [item for sublist in all_possible_pair.store_all_pos for item in sublist] #2
    set_sentence = [item for sublist in sentence_data for item in sublist] #3
    # from 1-3 I changed every list of list into list to turn them into 'set'
    set_sentence = set(set_sentence) # turn list of sentence into set
    set_vocab = set(store_raw_vocab)  # turn list of vocab into set
    intersec_bigram_and_vocab = set_sentence - set_vocab # now check the UNK in the sentence by substract the sentence with the set of vocab

    arr_sentence = []
    arr_intersec_bigram_and_vocab = []
    for s in sentence: # loop to add word in the sentence in to 'arr_sentence'
        arr_sentence.append([s])
    for s in intersec_bigram_and_vocab: # loop to add the words that are UNK in 'arr_intersec_bigram_and_vocab'
        arr_intersec_bigram_and_vocab.append([s])

    k = 0
    for i in arr_sentence:
        for j in arr_intersec_bigram_and_vocab:
            if i == j:
                del arr_sentence[k] # loop to delete that UNK word in the sentence
                arr_sentence.insert(k, ["UNK"]) # and insert "UNK" instead
        k = k + 1

    sort_list.new_sentence = [[]] # define list of list
    for s in arr_sentence: # now turn into list of list again with new value
        sort_list.new_sentence.append([s])

####### read the files by calling 'read_file' function and store the values in parameter as list######
read_sampledata = read_file('a01_data\sampledata.txt') #
read_sampledata_cover = read_file('a01_data\sampledata.txt')
sampledata_vocab = read_file('a01_data\sampledata.vocab.txt')
sentence_data = read_file('a01_data\sampletest.txt')
####### read the files by calling 'read_file' function and store the values in parameter as list######


vocab_lenght = len(sampledata_vocab) # 'vocab_lenght' as the 'sampledata_vocab' length
remove_cover(read_sampledata, "model") # call function 'remove_cover' to remove <s>, </s> of sample data
unk_count(vocab_lenght, remove_cover.data) # count the number of UNK by using function 'unk_count'
print("Training data (sampledata.txt) : ", read_sampledata_cover) #print the read files of 'read_sampledata_cover'
print("Vocabulary (sampledata.vocab.txt) : ", sampledata_vocab) #print the read files of 'sampledata_vocab'
print("UNK Found : ", unk_count.unk) # display the number of UNK
print("\nxxxxxxxxxxxxxx U N I G R A M xxxxxxxxxxxxxxxx (UNSMOOTHED)")
unigram_model(remove_cover.data, unk_count.unk) #calculate the UNIGRAM prob. of word using 'unigram_model' function
print("xxxxxxxxxxxxxx U N I G R A M xxxxxxxxxxxxxxxx (SMOOTHED)")
unigram_model_laplace(remove_cover.data, unk_count.unk, len(unk_count.list), 0, "false")  # calculate the UNIGRAM LAPLCE SMOOTHING prob. of word using 'unigram_model_laplace' function

print("\nxxxxxxxxxxxxxxxxx B I G R A M xxxxxxxxxxxxxxxxxxx (UNSMOOTHED)")
into_bigram_pair(read_sampledata_cover) # send the sample data without removing <s>, </s> to get pairs of BIGRAM MODEL
all_possible_pair() # now use the bigram data from above line to calculate all possible pairs in the bigram prob. table
bigram_unsmoothed(all_possible_pair.sampledata_cover, into_bigram_pair.data, all_possible_pair.unmatched_set)
# send all the information we got through the 'bigram_unsmoothed' function to calculate bigram unsmoothing prob.

print("\nxxxxxxxxxxxxxxxxx B I G R A M xxxxxxxxxxxxxxxxxxx (SMOOTHED)")
bigram_smoothed_laplace(all_possible_pair.sampledata_cover, into_bigram_pair.data, all_possible_pair.unmatched_set)
# call 'bigram_smoothed_laplace' function to calculate bigram laplace smoothing using the same information as unsmoothing used

print("\nxxxxxxxxxxxxxxx S E N T E N C E _ P R O B A B I L I T Y xxxxxxxxxxxxxxxxx")
print("Sentence Data(sampletest.txt) : ", sentence_data) #display the every sentences data in the sampletest.txt
remove_cover(sentence_data, "prob") #call 'remove_cover' to remove <s>, </s> from sentence data
sentence = read_file('a01_data\sampletest.txt')#read the files by calling 'read_file' function and store the values in 'sentence' as list
unigram_model_laplace(remove_cover.data, unk_count.unk, vocab_lenght, sentence_data[2], "true") #calculate the unigram laplace smoothing of sentence 3 using 'unigram_model_laplace'
print("Sentence no.3",sentence[2], "     : Unigram Prob. :", unigram_model_laplace.num) # print the result of sentence 3
unigram_model_laplace(remove_cover.data, unk_count.unk, vocab_lenght, sentence_data[3], "true") #calculate the unigram laplace smoothing of sentence 4 using 'unigram_model_laplace'
print("Sentence no.4",sentence[3], ": Unigram Prob. :", unigram_model_laplace.num) # print the result of sentence 4
unigram_model_laplace(remove_cover.data, unk_count.unk, vocab_lenght, sentence_data[4], "true") #calculate the unigram laplace smoothing of sentence 5 using 'unigram_model_laplace'
print("Sentence no.5",sentence[4], ": Unigram Prob. :", unigram_model_laplace.num) # print the result of sentence 5

sort_list(read_file('a01_data\sampletest.txt')) # call the 'sort_list' function to get new sentence information to use in another function
new_sentence = [item for sublist in sort_list.new_sentence for item in sublist] # turn the information from 'sort_list.new_sentence' into list named 'new_sentence'
into_bigram_pair(new_sentence) #now send the 'new_sentence' through 'into_bigram_pair' function
bigram_sentence_probabality(into_bigram_pair.data[10:14], bigram_smoothed_laplace.store_prob) # calculate bigram laplace smoothing prob. of sentence 3(array index) using function 'bigram_sentence_probabality'
print("Sentence no.3",sentence[2], "     : Bigram Prob. :", round((bigram_sentence_probabality.prob), 5)) #display the result of sentence 3 prob.
bigram_sentence_probabality(into_bigram_pair.data[14:19], bigram_smoothed_laplace.store_prob) # calculate bigram laplace smoothing prob. of sentence 4(array index) using function 'bigram_sentence_probabality'
print("Sentence no.4",sentence[3], ": Bigram Prob. :", round((bigram_sentence_probabality.prob), 5)) #display the result of sentence 3 prob.
bigram_sentence_probabality(into_bigram_pair.data[19:24], bigram_smoothed_laplace.store_prob) # calculate bigram laplace smoothing prob. of sentence 5(array index) using function 'bigram_sentence_probabality'
print("Sentence no.5",sentence[4], ": Bigram Prob. :", round((bigram_sentence_probabality.prob), 5)) #display the result of sentence 3 prob.

