from histogram import invert_hist
from clean_text import clean
import random

# def gen_sentence(source):
#     # text = clean(source)

#     word_count = 7
#     counter = 1
#     sentence = []
#     while counter <= word_count:
#         if counter == 1: # upper case the first character 
#             word1 = (stochastic_sample(source))
#             word = word1.capitalize()
#             sentence.append(word)
#             counter += 1
#             # print(word1)
#         # elif word_count > counter > 0 : # lowercase the rest? 
#         else: 
#             word2 = stochastic_sample(source)
#             sentence.append(word2.lower())
#             counter += 1

#          # add a period to the last word
#     period = "."
#     # counter += 1
#     # print(sentence)
#     sentence = " ".join(sentence)
#     sentence += period
#     print(sentence)
#     return sentence

def stochastic_sample(source):
    ''' Histogram -> percentages -> random item'''
    hist = invert_hist(source)
    percentages = {}
    # print(hist)
    text = clean(source)

    # with open(text) as file: 
    #     word_list = (file.read().split(" "))
    length = len(text)
    dart = random.randint(0, 100) # index is not length
    # print(length)
    # print(word_list)
    # print("dart: {}".format(dart))

# calculate total for percent 
    total = 0
    for item in hist: 
        total += (len(item[1]) * item[0])
        # print("len item: {}".format(len(item[1]))) # number of words per index
# individual percentages added to percent dict
    for item in hist:  
        for word in item[1]: 
            word_percentage = item[0]/total
            percentages[word] = word_percentage * 100

# finding the place the dart hit. each word has percentage assigned, we add them until we reach the dart
    num = 0
    target = None
    for word in percentages:
        num += percentages[word]
        target = word
        # print("trial - num: {}, target: {}".format(num, target)) #prints each trial through the hist
        if num > dart: # we add til we break it. if we cross the line, we return  
            break
    
    # print("num: {}, target: {}".format(num, target))
    # print('')
    # print(hist)
    # print('')
    # print(percentages)
    # print(target)
    # print(str(target))
    return str(target)

if __name__ == '__main__':
    stochastic_sample("source_text.txt")