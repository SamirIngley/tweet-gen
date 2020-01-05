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
    # print(len(rand_sentence))  why won't this work ??? 
    place = (markov.states)
    # print("PLACEEEE: {}".format(place['fish']))

    last_word = None
    counter = 0

    while counter < num_words:
        # print(length, num_words)
        if last_word == None:
            last_word = choice(list(place.keys()))
            # print("keys!! {}".format(list(place.keys())))
            # print(last_word)
            rand_sentence.append(last_word.capitalize())
            counter += 1

        else:
            # print(place.items())
            for item in place.items():
                if item[0] == last_word:
                    # print("item1s: {}".format(list(item[1])))
                    last_word = choice(list(item[1]))
                    # print(last_word)
                    rand_sentence.append(last_word) 
                    counter += 1
                    break
                else:
                    pass
    

    period = "."
    sentence = " ".join(rand_sentence)
    sentence += period
    # print(sentence)
         

    print(sentence)
    return 

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
    corpus = ("The ride of a lifetime by Robert Iger. The best book I read this year. A good example of a Nice guy coming first. What you do is who you are by Ben Horowitz. This book is going to make it fashionable to use the world “Culture” in boardrooms Who is Michael Ovitz by Michael Ovitz. A window into managing Hollywood talent - Future of managing top technical talent The dog who took me up a mountain by Rick Crandall .").split()
    # corpus2 = (source_text.txt).split()
    markov_instance = Markov(corpus)
    # print(markov_instance.states)
    # print(type(markov_instance.chain))
    random_walk(14, markov_instance)