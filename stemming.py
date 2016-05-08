from nltk.stem import PorterStemmer
from  nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words=["kajaed","kajaly","kajaish","kajaing"]

for i in example_words:
    print(ps.stem(i))