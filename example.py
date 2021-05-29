from ds_extraction.ahocorasick import Dictionary

if __name__ == '__main__':
    my_dict = Dictionary()
    sentence = '''
    spironolactone & an iud helpedd withh acne & pain but in 2013 i had an ovarian torsion requiring surgery & they saved my right ovary. 
    i began having hair loss from telogen effogen & reoccurant yeast infections- i was diagnosed as pre-diabetic & cut sugar our from my already low sugar diet. 
    fast forward to january of this yea i went to the er due to pain from another torsion on the right side & again the ovary was saved. i was put on ortho tricyclen lo & still have my iud & take the spironolactone but had horribly painful cysts last month which brought me to the er but with no torsion they did nothing. the pain has been intermitten since & is getting more severe. it feels like ice cubes in my ovaries & warm water/electic shocks down my thighs. 
    i had the hpv vaccine but my last pap showed up irregular & the biopsy of cysts got lost. 
    any thoughts on what happening?
    '''
    
    # Return list of disease and symptom
    d , s = my_dict.get_ner(sentence,mode='aho',correct=True)
    print(d,s)