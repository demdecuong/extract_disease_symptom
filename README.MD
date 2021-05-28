# Extract Diseases/Symptoms with Aho-corasik

## installation
`pip install -r requirement.txt`

## Features

### Build Dictionary
    python build_dict.py

The input is from `./data./entities.json`

The output dictionary will be stored in `./saved_dict`
### Usage
    from ahocorasik import Dictionary

    my_dict = Dictionary()
    sentence = '''
    Xin chào bác sĩ. tôi bị sốt, đau họng, chóng mặt. Không biết đó có phải là triệu chứng của ung thư gan không
    '''

    # Return list of disease and symptom
    d , s = my_dict.get_ner(sentence,mode='aho',correct=False)
    print(d,s)
    # Output
    # ['ung thư gan'] ['sốt', 'chóng mặt']

- There are 3 modes : `['aho','edit','ahoedit']`
    - aho : use aho-corasik to search in dict
    - edit : use edit-distance to search in dict
    - ahoedit : use both strategy then combine the result

- correct mode:
    - token correction by edit-distance
    - This mode currently support English 
### Evaluate on test set A
    python evaluate.py 

    # Output
    Total Accuracy 0.9532681824139623  
    Accuracy of Disease 1.0  
    Accuracy of Symptom 0.8675588196785163  