import spacy

if __name__ == '__main__':

    with open('data/raw/tweets.txt', 'r') as file:
        data = file.read().replace('\n', '')

    nlp = spacy.load("en_core_web_lg")

    # Created by processing a string of text with the nlp object, replace Hello Wordl! with tweets string
    doc = nlp(data)

    people = []
    
    # Iterate over tokens in a Doc
    for ent in doc.ents:
        # print(ent.text, ent.label_)
        if ent.label_ == 'PERSON':
            entity = ent.text + ' ' +  ent.label_ + '\n'
            people.append(entity)

    people_str = ' '.join(str(x) for x in people)
    file = open("data/processed/ents.txt", "w")
    file.write(people_str)
    file.close()
