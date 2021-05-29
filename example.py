from ds_extraction.ahocorasick import Dictionary

if __name__ == '__main__':
    my_dict = Dictionary()
    sentence = '''
    Xin chào bác sĩ. tôi bị sốt, đau họng, chóng mặt
    '''

    # Return list of disease and symptom
    d , s = my_dict.get_ner(sentence,mode='edit')
    print(d,s)