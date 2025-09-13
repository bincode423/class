from sklearn.preprocessing import OneHotEncoder
import numpy as np

words = np.array(['car', 'cat', 'dog', 'door', 'desk', 'display', 'door', 'dog', 'desk', 'display'])
encoder = OneHotEncoder(sparse_output=False)
one_hot = encoder.fit_transform(words.reshape(-1, 1))
print(one_hot)