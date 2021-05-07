from ahocorasik import Dictionary


if __name__ == '__main__':
    my_dict = Dictionary()
    sentence = '''
    Xin chào bác sĩ. tôi bị sốt, đau họng, chóng mặt. Không biết đó có phải là triệu chứng của ung thư gan không
    '''

    # Return list of disease and symptom
    d , s = my_dict.get_ner(sentence)
    print(d,s)