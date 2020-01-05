from flask import Flask
import sentence
from markov_chain import Markov, random_walk


app = Flask(__name__)

@app.route('/')
def sentences():
    # phrase = sentence.gen_sentence("source_text.txt")
    markov_instance = Markov("source_text.txt")
    random_walk(14, markov_instance)
    return random_walk
