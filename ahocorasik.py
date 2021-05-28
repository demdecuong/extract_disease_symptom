import pandas as pd
import ahocorasick

from utils.utils import read_dict, get_ngram, read
from edit_distance import Distance
from tqdm import tqdm 

class Dictionary:
    def __init__(self,di_path='./saved_dict/disease_dict',sy_path='./saved_dict/symptom_dict',n_gram = 5,di_threshold=0.8,sy_threshold=0.8):
        self.di_dict = read_dict(di_path)
        self.sy_dict = read_dict(sy_path)
        self.max_n_gram = n_gram
        self.distance = Distance()
        
        self.di_dict_list = list(self.di_dict.keys())
        self.sy_dict_list = list(self.sy_dict.keys())
        
        self.di_threshold = di_threshold
        self.sy_threshold = sy_threshold

    def get_ner(self,sentence,mode='aho'):
        assert mode in ['aho','edit','ahoedit']
        
        if mode == 'edit':
            disease, symptoms = self.get_ner_edit(sentence)
        
        elif mode == 'ahoedit':
            disease = []
            symptoms = []
            disease_aho, symptoms_aho = self.get_ner_aho(sentence)
            disease_edit, symptoms_edit = self.get_ner_edit(sentence)
            
            # Merging 2 list
            disease.extend(disease_aho)
            disease.extend(disease_edit)
            
            symptoms.extend(symptoms_aho)
            symptoms.extend(symptoms_edit)
            # Sort 

            disease = list(set(disease))
            symptoms = list(set(symptoms))
        else:
            disease, symptoms = self.get_ner_aho(sentence)
        
        return disease, symptoms

    def get_ner_aho(self,sentence):
        # Aho-corasik searching
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

    def get_ner_edit(self,sentence):
        # Edit-distance searching 
        disease = []
        symptoms = []
        for i in range(2,self.max_n_gram):
            ngrams = get_ngram(sentence,i)
            for item in tqdm(ngrams):
                text = ' '.join(item)
                for di in self.di_dict_list:
                    partial_score = self.distance.compare_word(text,di)['partial']
                    if partial_score > self.di_threshold:
                        disease.append(text)
                for sy in self.sy_dict_list:
                    partial_score = self.distance.compare_word(text,sy)['partial']
                    if partial_score > self.sy_threshold:
                        symptoms.append(text)    
        disease = list(set(disease))
        symptoms = list(set(symptoms))
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