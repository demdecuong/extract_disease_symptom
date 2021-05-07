import pandas as pd
import ahocorasick

from utils.utils import read_dict, get_ngram, read


class Dictionary:
    def __init__(self,di_path='./saved_dict/disease_dict',sy_path='./saved_dict/symptom_dict',n_gram = 5):
        self.di_dict = read_dict(di_path)
        self.sy_dict = read_dict(sy_path)
        self.max_n_gram = n_gram

    def get_ner(self,sentence):
        disease = []
        symptoms = []
        for i in range(1,self.max_n_gram):
            ngrams = get_ngram(sentence,i)
            for item in ngrams:
                text = ' '.join(item)
                if self.get_disease(text) != 'not_exists':
                    disease.append(text)
                if self.get_symptom(text) != 'not_exists':
                    symptoms.append(text)
        return disease, symptoms

    def get_disease(self,s):
        return self.di_dict.get(s,'not_exists')

    def get_symptom(self,s):
        return self.sy_dict.get(s,'not_exists')


if __name__ == '__main__':
    my_dict = Dictionary()

    data = pd.read_csv('./test_data/testB.csv',encoding='utf-8')
    data = data['question'].tolist()
    # data = read('./test_data/seq.in')
    disease = []
    symptom = []
    cnt = 0
    for sentence in data:
        d , s = my_dict.get_ner(sentence)
        if d != [] and s!=[]:
            cnt += 1
        if d == []:
            disease.append('not_exists')
        else:
            disease.append(d)
        if s == []:
            symptom.append('not_exists')
        else:
            symptom.append(s)

    print(len(data),len(disease),len(symptom))
    df = pd.DataFrame({
        'question': data,
        'disease': disease, 
        'symptom' : symptom,
    })
    df.to_csv('resultA.csv',encoding='utf-8')