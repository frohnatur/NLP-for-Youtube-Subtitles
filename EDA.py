import pickle
from collections import Counter
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix.pkl')
data = data.transpose()
print(data.head())

#Liste mit meist genutzten Wörtern erstellen
top_dict = {}
for column in data.columns:
    top = data[column].sort_values(ascending=False).head(30)
    top_dict[column] = list(zip(top.index, top.values))

for creator, top_words in top_dict.items():
    print(creator)
    print(', '.join([word for word, count in top_words[0:29]]))
    print('---')

#Welche meist genutzten Wörter werden von wie vielen Creatorn genutzt?
words = []
for creator in data.columns:
    top = [word for (word, count) in top_dict[creator]]
    for t in top:
        words.append(t)

print(Counter(words).most_common())

#Meist genutzte Wörter, die von mehr als der Hälfte benutzt werden entfernen und neue Dokument-Term-Matrix erstellen
add_stop_words = [word for word, count in Counter(words).most_common() if count > 1]
print(add_stop_words)

data_clean = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')

german_stopwords = list(stopwords.words('german'))
total_stopwords = list(set(add_stop_words + german_stopwords))

cv = CountVectorizer(stop_words=total_stopwords)
data_cv = cv.fit_transform(data_clean.subtitles)
data_stop = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_stop.index = data_clean.index

pickle.dump(cv, open("Corpus_Dokument-Term_Matrix/Count_Vektorizer_Total_Stopwords.pkl", "wb"))
data_stop.to_pickle("Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix_Total_StopWords.pkl")

print(data_stop)
data_stop = data_stop.transpose()
top_dict_stop = {}
for column in data_stop.columns:
    top = data_stop[column].sort_values(ascending=False).head(60)
    top_dict_stop[column] = list(zip(top.index, top.values))

for creator, top_words in top_dict_stop.items():
    print(creator)
    print(', '.join([word for word, count in top_words[30:59]]))
    print('---')

words_stop = []
for creator in data_stop.columns:
    top = [word for (word, count) in top_dict_stop[creator]]
    for t in top:
        words_stop.append(t)

print(Counter(words_stop).most_common())

data_clean_extended = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')
data_clean_extended['length'] = data_clean_extended['subtitles'].astype(str).apply(len)
data_clean_extended['word_count'] = data_clean_extended['subtitles'].apply(lambda x: len(str(x).split()))
print(data_clean_extended['length'].head())
print(data_clean_extended['word_count'].head())

#Wie viele einzigartige Wörter werden benutzt
unique_list = []
for creator in data.columns:
    uniques = data[creator].to_numpy().nonzero()[0].size
    unique_list.append(uniques)

creators = ["HandOfBlood", "PietSmiet", "Maxim", "GrummelFritz", "Beam"]

data_words = pd.DataFrame(list(zip(creators, unique_list)), columns=['creator', 'unique_words'])
data_unique_sort = data_words.sort_values(by='unique_words', ascending=False)

print(data_unique_sort)

y_pos = np.arange(len(data_words))

plt.barh(y_pos, data_unique_sort.unique_words, align='center')
plt.yticks(y_pos, data_unique_sort.creator)
plt.title('Anzahl einzigartiger Wörter', fontsize=20)

plt.show()

#wie viele signature words im vergleich zu 'scheiße' werden benutzt
data_signature_words = data.transpose()[['scheiße', 'gott', 'alter', 'geil']]
data_signature_words= pd.concat([data_signature_words.scheiße, data_signature_words.gott + data_signature_words.alter + data_signature_words.geil], axis=1)
data_signature_words.columns = ['scheiße', 'signature']
print(data_signature_words)

plt.rcParams['figure.figsize'] = [5, 5]

for i, creator in enumerate(data_signature_words.index):
    x = data_signature_words.scheiße.loc[creator]
    y = data_signature_words.signature.loc[creator]
    plt.scatter(x, y, color='blue')
    plt.text(x - 20, y - 20, creators[i], fontsize=10)
    plt.xlim(-5, 500)

plt.title('Anzahl Schimpf- und Signaturwörter', fontsize=20)
plt.xlabel('Anzahl \"scheiße\"', fontsize=15)
plt.ylabel('Anzahl Signaturwörter', fontsize=15)

plt.show()