from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("dogs"))
print(lemmatizer.lemmatize("hen"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("person"))
print(lemmatizer.lemmatize("walking", pos="v"))


##better than stemming , you get an actual word
