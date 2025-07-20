# Download Haiku dataset from from https://www.kaggle.com/datasets/hjhalani30/haiku-dataset
import csv
import spacy
import random

nlp = spacy.load("en_core_web_sm")
data = []

def extract_keywords(text, top_k=1):
    doc = nlp(text)
    # Get only NOUNs or PROPNs that are not stopwords
    keywords = [token.text.lower() for token in doc if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop]
    return list(set(keywords)) if keywords else ["life"]  # fallback keyword


with open('all_haiku.csv') as f:
    reader = csv.reader(f)
    c = 0
    for row in reader:
        if row[4] == 'twaiku':
            c += 1
            if not c % 100: print('Created ' + str(c) + ' samples')
            if c == 1000: break
            haiku = '\n'.join([i.strip() for i in row[1:-2]])
            keywords = ', '.join(extract_keywords(haiku))
            sample = '### prompt: ' + keywords + '\n' + haiku + '\n\n'
            data.append(sample)

with open('input.txt', 'w') as f:
   for i in range(10):
       random.shuffle(data)
       f.write(''.join(data))
