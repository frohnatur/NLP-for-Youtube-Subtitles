import pandas as pd
from textblob_de import TextBlobDE
import matplotlib.pyplot as plt
import numpy as np
import math

import seaborn as sns

#data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')

#HandOfBloodStatsSubtitles = pd.read_csv('VideoStatisiken/HandOfBloodStatsSubtitles', index_col=0)
#PietSmietStatsSubtitles = pd.read_csv('VideoStatisiken/PietSmietStatsSubtitles', index_col=0)
#MaximStatsSubtitles = pd.read_csv('VideoStatisiken/MaximStatsSubtitles', index_col=0)
#GrummelFritzStatsSubtitles = pd.read_csv('VideoStatisiken/GrummelFritzStatsSubtitles', index_col=0)
#BeamStatsSubtitles = pd.read_csv('VideoStatisiken/BeamStatsSubtitles', index_col=0)


creators = ["HandOfBlood", "PietSmiet", "Maxim", "GrummelFritz", "Beam"]

polarity = lambda x: TextBlobDE(x).sentiment.polarity
subjectivity = lambda x: TextBlobDE(x).sentiment.subjectivity

#HandOfBloodStatsSubtitles['subjectivity'] = HandOfBloodStatsSubtitles['subtitles'].apply(subjectivity)
#HandOfBloodStatsSubtitles['polarity'] = HandOfBloodStatsSubtitles['subtitles'].apply(polarity)
#HandOfBloodStatsSubtitles.to_csv('VideoStatisiken/HandOfBloodPolSubj')

#PietSmietStatsSubtitles['subjectivity'] = PietSmietStatsSubtitles['subtitles'].apply(subjectivity)
#PietSmietStatsSubtitles['polarity'] = PietSmietStatsSubtitles['subtitles'].apply(polarity)
#PietSmietStatsSubtitles.to_csv('VideoStatisiken/PietSmietPolSubj')

#MaximStatsSubtitles['subjectivity'] = MaximStatsSubtitles['subtitles'].apply(subjectivity)
#MaximStatsSubtitles['polarity'] = MaximStatsSubtitles['subtitles'].apply(polarity)
#MaximStatsSubtitles.to_csv('VideoStatisiken/MaximPolSubj')

#GrummelFritzStatsSubtitles['subjectivity'] = GrummelFritzStatsSubtitles['subtitles'].apply(subjectivity)
#GrummelFritzStatsSubtitles['polarity'] = GrummelFritzStatsSubtitles['subtitles'].apply(polarity)
#GrummelFritzStatsSubtitles.to_csv('VideoStatisiken/GrummelFritzPolSubj')

#BeamStatsSubtitles['subjectivity'] = BeamStatsSubtitles['subtitles'].apply(subjectivity)
#BeamStatsSubtitles['polarity'] = BeamStatsSubtitles['subtitles'].apply(polarity)
#BeamStatsSubtitles.to_csv('VideoStatisiken/BeamPolSubj')

#data['subjectivity'] = data['subtitles'].apply(subjectivity)
#data['polarity'] = data['subtitles'].apply(polarity)
#data.to_pickle("Corpus_Dokument-Term_Matrix/PolSubj.pkl")

HandOfBloodPolSubj = pd.read_csv('VideoStatisiken/HandOfBloodPolSubj')
PietSmietSubtitlesPolSubj = pd.read_csv('VideoStatisiken/PietSmietPolSubj')
MaximPolSubj = pd.read_csv('VideoStatisiken/MaximPolSubj')
GrummelFritzPolSubj = pd.read_csv('VideoStatisiken/GrummelFritzPolSubj')
BeamPolSubj = pd.read_csv('VideoStatisiken/BeamPolSubj')

creator_list = [(HandOfBloodPolSubj, "HandOfBlood"), (PietSmietSubtitlesPolSubj, "PietSmiet"), (MaximPolSubj, "Maxim"),
                (GrummelFritzPolSubj, "GrummelFritz"), (BeamPolSubj, "Beam")]

fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(20, 90), sharey=True)
fig.subplots_adjust(hspace=.8, wspace=.3)
i = 0
for creator in creator_list:
    sns.lineplot(data=creator[0], ax=axes[i][0], x=creator[0].index, y='polarity').set(title=creator[1],xlabel="Video",ylabel="Polarität")
    sns.scatterplot(data=creator[0], ax=axes[i][1], x='polarity', y='likeCount').set(title=creator[1],xlabel="Polarität", ylabel="Likes")
    i = i+1

plt.show()

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