import seaborn as sns
import pandas as pd
import numpy as np
import sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
import pickle
from joblib import dump, load

df = pd.read_csv("bigdat.csv")
speech = df["speech"].tolist()
count_vect = CountVectorizer()
party = df["party"].tolist()
x_train_counts = count_vect.fit_transform(speech)
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
train_x, test_x, train_y, test_y = train_test_split(x_train_tfidf, party, test_size=0.1)
clf = SVC(kernel='linear').fit(train_x, train_y)
y_score = clf.predict(test_x)
print(test_x)

n_right = 0
for i in range(len(y_score)):
    if y_score[i] == test_y[i]:
        n_right += 1

print("Accuracy: %.2f%%" % ((n_right/float(len(test_y)) * 100)))
dump(clf, 'glow.joblib')
with open('countvec.pk', 'wb') as fin:
    pickle.dump(count_vect, fin)
with open('tfidf.pk', 'wb') as chin:
    pickle.dump(tfidf_transformer, chin)
