import re
import spacy

nlp = spacy.load("en_core_web_sm") 


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    doc = nlp(text)
    text = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return text
