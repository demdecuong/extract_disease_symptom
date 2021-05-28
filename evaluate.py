import ast
import pandas as pd
from ahocorasick import Dictionary
from utils.utils import read_dict, get_ngram, read, get_entities, save


if __name__ == '__main__':
    my_dict = Dictionary()

    data = read('./test_data/seq.in')
    label = read('./test_data/seq.out')
    gold = read('./test_data/gold_entities.txt')

    # disease = []
    # symptom = []
    # cnt = 0
    # for sentence, label in zip(data,gold):
    #     d , s = my_dict.get_ner(sentence)
    #     if gold in d or s in gold:
    #         cnt += 1
    #     if d == []:
    #         disease.append('not_exists')
    #     else:
    #         disease.append(d)
    #     if s == []:
    #         symptom.append('not_exists')
    #     else:
    #         symptom.append(s)
   
    # print(len(data),len(disease),len(symptom),len(gold))


    # df = pd.DataFrame({
    #     'question': data,
    #     'disease': disease, 
    #     'symptom' : symptom,
    #     'target_entites' : gold,
    # })
    # df.to_csv('./result/resultA.csv',encoding='utf-8')

    data = pd.read_csv('result/resultA.csv')

    disease = data['disease'].tolist()
    symptom = data['symptom'].tolist()
    target = data['target_entites'].tolist()
    cnt_disease = 0
    cnt_symptom = 0
    disease_case = 0
    symptom_case = 0
    acc = 0
    for i in range(len(disease)):
        # check disease
        a= 0.0
        b= 0

        if target[i] == 'None':
            if disease[i] == 'not_exists':
                a = 1
            else: 
                a = 0
            if symptom[i] == 'not_exists':
                b = 1
            else:
                b = 0
            symptom_case += 1
            disease_case += 1
            cnt_disease += a
            cnt_symptom += b
        else:
            if ',' in target[i]:
                if symptom[i]== 'not_exists':
                    symptom[i] == ['not_exists']
                else:
                    symptom[i] = ast.literal_eval(symptom[i])
                g = target[i].split(',')
                g = [item.strip() for item in g]            
                for ii in symptom[i]:
                    if ii in g:
                        b += 1
                b = b / len(g)
                a = 1

                symptom_case += 1
                cnt_symptom += b
            else:
                b = 1
                if target[i] in disease[i]:
                    a = 1
                cnt_disease += a
                disease_case += 1

        acc += ((a+b)/2)

    print("Evaluate on Test Set A")
    print("Total Accuracy",acc/len(target))
    print("Accuracy of Disease",cnt_disease/disease_case)
    print("Accuracy of Symptom",cnt_symptom/symptom_case)