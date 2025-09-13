import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

similar_words = model.most_similar("dog", topn=5)
print(similar_words)

s1 = model.similarity("dog", "bear")
s2 = model.similarity("dog", "car")

print("dog vs bear:", s1)
print("dog vs car:", s2)