import pandas as pd
from textblob_de import TextBlobDE
import matplotlib.pyplot as plt
import numpy as np
import math

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')
creators = ["HandOfBlood", "PietSmiet", "Maxim", "GrummelFritz"]

polarity = lambda x: TextBlobDE(x).sentiment.polarity
subjectivity = lambda x: TextBlobDE(x).sentiment.subjectivity

#data['subjectivity'] = data['subtitles'].apply(subjectivity)
#data['polarity'] = data['subtitles'].apply(polarity)

print(data)

#data.to_pickle("Corpus_Dokument-Term_Matrix/PolSubj.pkl")

plt.rcParams['figure.figsize'] = [10, 8]

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/PolSubj.pkl')

for index, creator in enumerate(data.index):
    x = data.polarity.loc[creator]
    y = data.subjectivity.loc[creator]
    plt.scatter(x, y, color='blue')
    plt.text(x + .001, y - .001, creators[index], fontsize=10)
    plt.xlim(-.2, .5)

plt.title('Sentiment Analysis', fontsize=20)
plt.xlabel('<-- Negativ -------- Positiv -->', fontsize=12)
plt.ylabel('<-- Fakten -------- Meinung -->', fontsize=12)

plt.show()

def split_text(text, n=10):

    length = len(text)
    size = math.floor(length / n)
    start = np.arange(0, length, size)

    split_list = []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece] + size])
    return split_list


list_pieces = []
for t in data.subtitles:
    split = split_text(t)
    list_pieces.append(split)


print(len(list_pieces))
print(len(list_pieces[0]))

polarity_subtitles = []
for lp in list_pieces:
    polarity_piece = []
    for p in lp:
        polarity_piece.append(TextBlobDE(p).sentiment.polarity)
    polarity_subtitles.append(polarity_piece)

plt.rcParams['figure.figsize'] = [10, 8]

for index, creator in enumerate(data.index):
    plt.subplot(3, 4, index + 1)
    plt.plot(polarity_subtitles[index])
    plt.plot(np.arange(0, 10), np.zeros(10))
    plt.title(creators[index])
    plt.ylim(ymin=-.2, ymax=0.5)

plt.show()