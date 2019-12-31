
def clean(source):
    
    clean = []
    # opens and closes file properly
    with open(source) as file: 
        word_list = (file.read().split())
        # print(word_list)

        # removes punctuation and makes all lowercase
        punctuations = '''()[]{};:'"\<>/?@#$%^&*_~.'''
        # removed punct: - , !

        for word in word_list:
            string = []
            for char in word:
                if char not in punctuations:
                    string += char.lower()      # lowercase char added to string
            string = ''.join(string)            # chars joined together
            clean.append(string)                # individual strings added to clean ['blah', 'blah', ...]
        # clean = ' '.join(clean)               # turns into one big string

    # print(clean)
    return clean

if __name__ == '__main__':
    clean("source_text.txt")
