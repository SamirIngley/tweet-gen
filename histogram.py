# import sys
from clean_text import clean

def invert_hist(source):
    text = clean(source)
    # print(text)
    histogram = []
    # text = separate(text)
    word_cache = []
    instance_cache = []
    hist_cache = []


    for word in text:
        num_occur = 0
        # print(type(word))
        if word not in word_cache: # counts occurances of unique words
            word_cache.append(word)
            for word2 in text:
                if word == word2: 
                    num_occur += 1 
            instance = [num_occur, word]
            instance_cache.append(instance)              
        else: pass

    for item in instance_cache:
        lst = []
        if item[1] not in hist_cache:
            for item2 in instance_cache:
                if item[0] == item2[0]:
                    hist_cache.append(item2[1])
                    lst.append(item2[1])
            tup = (item[0], lst)
            histogram.append(tuple(tup))
            
    return histogram



def dict_hist(source):
    '''opens a text file
        creates empty dictionary
        appends null instance and adds 1 
        or adds 1 to the existing instance 
    '''
    histogram = {}    
    text = clean(source)
    
        # print(text)
    for word in text:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1
    # print(histogram)  
    return histogram



def list_hist(source):
    text = clean(source)


    histogram = []

    for word in text:
        instance = [word, 0]
        for word2 in text:
            if word == word2:
                instance[1] += 1
        if instance not in histogram:
            histogram.append(instance)
    # print(histogram)
    return histogram
        


def tuple_hist(source):
    text = clean(source)

    histogram = []
    # text = separate(text) 
    cache = []

    for word in text:
        if word not in cache:
            cache.append(word)
            num_occur = 0
            for word2 in text:
                if word2 == word:
                    num_occur += 1
            instance = (word, num_occur)
            tup = tuple(instance)
            histogram.append(tup)

    return histogram





def unique_words(histo):
    ''' returns length of histogram
    '''
    number = (len(histo))
    print("unique words: {}".format(number))
    return number


def frequency(word, histo):
    ''' returns number associated with word in histo
    '''
    freq = 0
    for item in histo:
        if item[0] == word:
            freq = item[1]
    print("freq of {}: {}".format(word, freq))
    return freq





if __name__ == '__main__':
    dicto_histo = dict_hist("source_text.txt")
    listo_histo = list_hist("source_text.txt")
    tuple_histo = tuple_hist("source_text.txt")
    invert_histo = invert_hist("source_text.txt")
    print(" ")
    print("INVERT: ", invert_histo)
    print(" ")
    print("TUP: ", tuple_histo)
    print(" ")
    print("DICTO: ", dicto_histo)
    print(" ")
    print("LIST: ", listo_histo)
    print(" ")
    unique_words(listo_histo)
    frequency("'the'", listo_histo)
    print(" ")
