text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

data = text.split()

textset = set()

for word in data:
    textset.add(word)

preps_used = textset.intersection(prepositions)

print(preps_used)