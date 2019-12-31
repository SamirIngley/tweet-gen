import random

def dictionary_words(num):
    file = open("/usr/share/dict/words", "r")
    words_list = (file.read().split('\n')) #.read gives whole file, .split splits a string into a list 
    new_list = []
    for word in range(num):
        new_list.append(random.choice(words_list))
    return(' '.join(new_list))

if __name__ == '__main__':
    print(dictionary_words(3))
    