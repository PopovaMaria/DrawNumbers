import sys
import random

articles = ['the', 'a', 'an']
nouns = ['cat', 'dog', 'man', 'women', 'child']
verbs = ['sang', 'ran', 'jumped']
adverbs = ['loudly', 'quietly', 'well', 'badly']

if sys.argv[1]:
    if int(sys.argv[1]) <= 10 and int(sys.argv[1]) >= 1:
        stringsamount = int(sys.argv[1])
    else:
        stringsamount = 5
else:
    stringsamount = 5

for number in range(stringsamount):
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    structure1 = [article, noun, verb, adverb]
    structure2 = [article, noun, verb]
    structure = random.randint(0,1)
    if structure:
        for item in structure1: print(item, end=' ')
    else:
        for item in structure2: print(item, end=' ',)
    print(' ')
