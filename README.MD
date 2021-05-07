# Extract Diseases/Symptoms with Aho-corasik

## installation
`pip install pyahocorasick`

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
    d , s = my_dict.get_ner(sentence)
    print(d,s)

Dictionary is in `ahocorasik.py`