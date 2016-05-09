import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_txt = state_union.raw("2005-GWBush.txt")
sample_txt = state_union.raw("2006-GWBush.txt")
customized_sent_tokenizer = PunktSentenceTokenizer(train_txt)
tokenized = customized_sent_tokenizer.tokenize(sample_txt)

for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    print(tagged)
