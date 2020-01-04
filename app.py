from flask import Flask
import sentence

app = Flask(__name__)

@app.route('/')
def sentences():
    phrase = sentence.gen_sentence("source_text.txt")
    return phrase