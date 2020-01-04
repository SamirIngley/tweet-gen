import sample


def gen_sentence(source, words):
    # text = clean(source)

    counter = 1
    sentence = []
    while counter <= words:
        if counter == 1: # upper case the first character 
            word1 = (sample.stochastic_sample(source))
            word = word1.capitalize()
            sentence.append(word)
            counter += 1
            # print(word1)
        # elif word_count > counter > 0 : # lowercase the rest? 
        else: 
            word2 = sample.stochastic_sample(source)
            sentence.append(word2.lower())
            counter += 1

         # add a period to the last word
    period = "."
    # counter += 1
    # print(sentence)
    sentence = " ".join(sentence)
    sentence += period
    print(sentence)
    return sentence


if __name__ == '__main__':
    gen_sentence("source_text.txt", 8)