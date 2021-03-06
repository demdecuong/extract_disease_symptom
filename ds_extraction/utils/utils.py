import re
import json
import pickle
import string

from nltk import ngrams


def read(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(line.replace('\n',''))
    return data

def save(data,path):
    textfile = open(path, "w")
    for element in data:
        textfile.write(element + "\n")


def read_dict(path):
    with open(path,'rb') as file:
        data = pickle.load(file)
    return data
    
def save_dict(data,path):
    with open(path, 'wb') as file:
        pickle.dump(data, file)

def get_ngram(sentence, n = 1):
    sentence = tokenize(sentence)
    return ngrams(sentence.split(' '), n)

def padding_punct(s):
    s = s.replace('\n', '').strip()
    s = re.sub('([.,!?()],"")', r' \1 ', s)
    s = re.sub('\s{2,}', ' ', s)
    return s

def tokenize(sentence):
    sent = sentence.replace('\n','').strip()
    sent = re.sub('(?<! )(?=[.,!?()])|(?<=[.,!?()])(?! )', r' ', sent)
    return sent

def get_entities(mess,preds):
    entities = []
    tmp = []
    for token,label in zip(mess,preds):
        if 'B' in label or 'I' in label:
            tmp.append(token)
        elif label=='O' and tmp != []:
            if len(tmp) > 1:
                tmp= ' '.join(tmp)
            else:
                tmp = tmp[0]
            entities.append(tmp)
            tmp = [] 
    if tmp != []:
        if len(tmp) > 1:
            tmp= ' '.join(tmp)
        else:
            tmp = tmp[0]
        entities.append(tmp)
        tmp = []

    return entities