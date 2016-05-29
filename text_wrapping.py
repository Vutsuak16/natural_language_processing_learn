# getting output in tabular form
from textwrap import fill

echoes = ["overhead", "the", "albatross", "hangs", "motionless", "upon", "the", "air"]
format = '%s(%d),'
pieces = [format % (word, len(word)) for word in echoes]
output=' '.join(pieces)
print(pieces)
print(output)
print(fill(output))