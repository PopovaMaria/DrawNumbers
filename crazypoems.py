import random

articles = ['the', 'a', 'an']
nouns = ['cat', 'dog', 'man', 'women', 'child']
verbs = ['sang', 'ran', 'jumped']
adverbs = ['loudly', 'quietly', 'well', 'badly']


for number in range(10):
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
