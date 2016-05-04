from collections import deque

f = open("calculus.txt")
paragraph = f.read().lower().split()
print(paragraph)
stop_words = ['the', 'that', 'to', 'as', 'there', 'has', 'and', 'or', 'is', 'not', 'a', 'of', 'but', 'in', 'by', 'on',
              'are', 'it', 'if']
paragraph = deque(paragraph)
x = [w for w in paragraph if w not in stop_words]
print(x)
print("the length of paragraph is " + str(len(paragraph)))
print("the length of  reduced paragraph without stop words " + str(len(x)))
