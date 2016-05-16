from nltk import FreqDist
import nltk
# solves problem given in text 61 of nltk book

puzzle_letters = FreqDist("egivrvonl")
obligatory='r'
wordlist=nltk.corpus.words.words()
l=[w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]
for i in l:
    print(i,end=" ")