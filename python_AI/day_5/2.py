from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

corpus = ['The dog ate the apple', 'The dog was angry', 'The dog was happy']
vect = CountVectorizer()
X = vect.fit_transform(corpus)
print(vect.get_feature_names_out())
print(X.toarray())