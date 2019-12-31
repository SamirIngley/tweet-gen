from flask import Flask
import random
import sample

app = Flask(__name__)

@app.route('/')
def sentences():
    sentence = sample.gen_sentence("source_text.txt")
    return sentence