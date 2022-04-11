import spacy
import re
import json
import PyPDF2


# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

with open('FinProj/tweets.json', 'rb') as f:

  tweets = json.load(f)

print(tweets)

miserables = open("miserables.txt", "rb")
miserables = miserables.read().decode("UTF-8")

miserables_sentences = re.split(r' *[\.\?!][\'"\)\]]* *', miserables)

print(miserables_sentences)

# happy, sad, angry, neutral

