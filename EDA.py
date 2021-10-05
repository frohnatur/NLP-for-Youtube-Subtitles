import pandas as pd
import pickle
from collections import Counter
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
print(german_stopwords)
total_stopwords = list(set(add_stop_words + german_stopwords))
print(total_stopwords)

cv = CountVectorizer(stop_words=total_stopwords)
data_cv = cv.fit_transform(data_clean.subtitles)
data_stop = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_stop.index = data_clean.index

pickle.dump(cv, open("Corpus_Dokument-Term_Matrix/Count_Vektorizer_Total_Stopwords.pkl", "wb"))
data_stop.to_pickle("Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix_Total_StopWords.pkl")

print(data_stop)
data_stop = data_stop.transpose()
#data_stop.to_csv('data_stop.csv', encoding='utf-8')
top_dict_stop = {}
for column in data_stop.columns:
    top = data_stop[column].sort_values(ascending=False).head(30)
    top_dict_stop[column] = list(zip(top.index, top.values))

words_stop = []
for creator in data_stop.columns:
    top = [word for (word, count) in top_dict_stop[creator]]
    for t in top:
        words_stop.append(t)

print(Counter(words_stop).most_common())

