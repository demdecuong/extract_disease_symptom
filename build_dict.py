import ahocorasick
import pickle
import json
import ast

from utils.utils import read, save, read_dict, save_dict 

def read(path):
    data = []
    with open(path,'r') as f:
        for line in f:
            data.append(line.replace('\n',''))
    return data

def build_entities(path='./data/entities.json'):
    '''
    Input:
        path : string 
            Path stores entites
    Return:
        disease = {}
        symptoms = {}
    '''
    with open(path) as f:
        data = f.read()
    data = ast.literal_eval(data)
    disease = data['DISEASE']
    symptoms = data['SYMPTOMS']
    diag = data['DIAG']
    overview = data['OVERVIEW']

    disease_ent = []
    symptom_ent = []
    for k in disease.keys():
        disease_ent.extend(disease[k])

    for k in symptoms.keys():
        symptom_ent.extend(symptoms[k])
    for k in diag.keys():
        symptom_ent.extend(diag[k])
    for k in overview.keys():
        symptom_ent.extend(overview[k])

    hhh_symptom = read('./data/symptoms.txt')
    hhh_disease = read('./data/disease.txt')
    symptom_ent.extend(hhh_symptom)
    disease_ent.extend(hhh_disease)
    print("Saving entites to file ...")
    save(disease_ent,'data/disease_entities.txt')
    save(symptom_ent,'data/symptom_entities.txt')

def build_dict(di_path='./data/disease_entities.txt',sy_path='./data/symptom_entities.txt'):
    
    disease_entities = read(di_path)
    symptom_entities = read(sy_path)

    disease_dict = ahocorasick.Automaton()
    symptom_dict = ahocorasick.Automaton()
    
    idx = 0
    for key in disease_entities:
        if disease_dict.get('cat', 'not_exists') == 'not_exists':
            disease_dict.add_word(key, (idx, key))
            idx += 1

    idx = 0
    for key in symptom_entities:
        if symptom_dict.get('cat', 'not_exists') == 'not_exists':
            symptom_dict.add_word(key, (idx, key))
            idx += 1    

    disease_dict.make_automaton()    
    symptom_dict.make_automaton()    

    print('Saving dictionary ...')
    with open('./saved_dict/disease_dict', 'wb') as file:
        pickle.dump(disease_dict, file)

    with open('./saved_dict/symptom_dict', 'wb') as file:
        pickle.dump(symptom_dict, file)

# print(B.get('cat', 'not exists'))
# print(B.get('minh','not exists'))
# print(B.get('she'))

if __name__ == '__main__':
    build_entities()
    build_dict()    
