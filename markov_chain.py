from random import choice
from pprint import pprint
from dictogram import Dictogram
from listogram import Listogram


class Markov:
    def __init__(self, corpus):
        self.corpus = corpus
        self.states = {}
        self.chain()

    def chain(self):
        last_word = None
        # Loop over all words in the corpus
        for word in self.corpus:
            # Skip the first iteration if we don't have a last_word
            if last_word is not None:
                # If we haven't seen last_word before
                if last_word not in self.states:
                    # Create a new empty histogram object as value
                    self.states[last_word] = Dictogram()
                # Add a count for the next word after last_word
                self.states[last_word].add_count(word)
            # Keep track of this word for the next iteration
            last_word = word
    
    def __str__(self):
        return str(self.states)


def random_walk(num_words, markov):
    rand_sentence = []
    length = len(rand_sentence)
    print(len(rand_sentence))
    place = (markov.states)
    # print("PLACEEEE: {}".format(place['fish']))
    last_word = None
    rand_sentence.append('hello')
    rand_sentence.append('wassa')


    # while len(rand_sentence) <= num_words:
    #     print(length, num_words)
    #     if last_word == None:
    #         for item in place.items():
    #             last_word = choice(list(place.keys()))
    #             print("keys!! {}".format(list(place.keys())))
    #             print(last_word)
    #             rand_sentence.append(last_word) 

    #     elif item[0] == last_word:
    #         for item in place.items():
    #             print("item1s: {}".format(list(item[1])))
    #             last_word = choice(list(item[1]))
    #             print(last_word)
    #             rand_sentence.append(last_word) 

    #     else:
    #         pass    


         

    # for item in range(num_words):
    #     words = []
    #     new_word = None
    #     if rand_sentence == None:
    #         for word in place:
    #             words.append(word)
    #     else: 
    #         print(place['fish'])

            # for word in place[new_word]:
            #     print("PLACE: {}".format(word))
            #     words.append(word)

        # new_word = choice(words)
        # rand_sentence.append(new_word)

        # print(' ********** ')
        # print("sentence: {}".format(rand_sentence))
        # print("words: {}".format(words))
        # print("new_word: {}".format(new_word))
        # print('************')

    # while length < words:
    # if length == 0:
    #     keys = {}
    #     for (key, value) in enumerate(markov.states):
    #         print(key, value)
    #         keys[key] = value
    #     rand_key = choice(keys)
    #     print(keys)
    #     print(rand_key)
    #     rand_sentence.append(rand_key)
    # else: 
    #     keys2 = {}
    #     for (key, value) in enumerate(markov.states):
    #         keys2[key] = value
            


        #     keys2 = []
        #     for (key, value) in new_word:
        #         print(key, value)
        #         keys2.append(key)
        #     rand_num = choice(keys2)
        #     print(rand_num)
        #     new_word = keys2[rand_num]
        #     rand_sentence.append(new_word)
        #     print(new_word)

    print(rand_sentence)
    return 

    # for state in markov.states:

    #     rando = 
    #     new_word = rando
    #     rand_sentence.append(new_word)


    #     print(state)
    # return 


# def random_walk(words, markov):
#     """Use random words to create a sentence"""
#     sentence = [] 
#     random_key = [key for key in markov.keys()]
#     # print(random_key)

#     i = 0
#     while i < 5:
#         output = choice(random_key)
#         # psrint(output)
#         sentence.append(output)
#         i += 1

#     return " ".join(sentence)

# def second_order_markov(words):
#     states ={}

#     for i in range(len(words) -2):
#         first_word = words[i]
#         second_word = words[i +1]
#         # pairs = (first_word, second_word)
#         # print(pairs)
#         third_word = words[i + 2]
#         # states[first_word] = markov_dict
#         if first_word not in states.keys():
#             histo = []
#             states[(first_word, second_word)] = histo
            
            
#         states[(first_word, second_word)].append(third_word)
         
#     values = states.items()
#     for key, value in values:
#         # markov_dict = {}  # can't use a regular dict
#         states[key] = Dictogram(value)  # to use a dictogram method (add_count), we must first establish a Dictogram() object
#         # markov_dict.add_count(second_word)
#         # print(markov_dict)
#     return states
#     # print(states)



if __name__ == '__main__':
    corpus = ("one fish two fish red fish blue fish").split(' ')

    markov_instance = Markov(corpus)
    print(markov_instance.states)
    print(type(markov_instance.chain))


    random_walk(10, markov_instance)