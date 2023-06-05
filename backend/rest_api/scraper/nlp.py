import spacy

def get_names(string):

    nlp = spacy.load("en_core_web_lg")

    # Created by processing a string of text with the nlp object, replace Hello Wordl! with tweets string
    doc = nlp(string)

    people = []
    
    # Iterate over tokens in a Doc
    for ent in doc.ents:
        # print(ent.text, ent.label_)
        if ent.label_ == 'PERSON':
            # entity = ent.text + ' ' +  ent.label_ + '\n'
            entity = ent.text
            people.append(entity)

    # people_str = ' '.join(str(x) for x in people)
    # file = open("data/processed/ents.txt", "w")
    # file.write(people_str)
    # file.close()
    # return people_str
    return people