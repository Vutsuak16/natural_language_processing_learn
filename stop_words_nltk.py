from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = " This love has taken its toll on me, she saying goodbye too many times before"

stopwords = set(stopwords.words("english"))

example_sentence_tokenized = word_tokenize(example_sentence)

print(stopwords)

print([w for w in example_sentence_tokenized if w not in stopwords])
