import pandas as pd
from textblob_de import TextBlobDE
import matplotlib.pyplot as plt
import numpy as np
import math

import seaborn as sns

# data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')

# HandOfBloodStatsSubtitles = pd.read_csv('VideoStatisiken/HandOfBloodStatsSubtitles', index_col=0)
# PietSmietStatsSubtitles = pd.read_csv('VideoStatisiken/PietSmietStatsSubtitles', index_col=0)
# MaximStatsSubtitles = pd.read_csv('VideoStatisiken/MaximStatsSubtitles', index_col=0)
# GrummelFritzStatsSubtitles = pd.read_csv('VideoStatisiken/GrummelFritzStatsSubtitles', index_col=0)
# BeamStatsSubtitles = pd.read_csv('VideoStatisiken/BeamStatsSubtitles', index_col=0)


creators = ["HandOfBlood", "PietSmiet", "Maxim", "GrummelFritz", "Beam"]

polarity = lambda x: TextBlobDE(x).sentiment.polarity
subjectivity = lambda x: TextBlobDE(x).sentiment.subjectivity

# HandOfBloodStatsSubtitles['subjectivity'] = HandOfBloodStatsSubtitles['subtitles'].apply(subjectivity)
# HandOfBloodStatsSubtitles['polarity'] = HandOfBloodStatsSubtitles['subtitles'].apply(polarity)
# HandOfBloodStatsSubtitles.to_csv('VideoStatisiken/HandOfBloodPolSubj')

# PietSmietStatsSubtitles['subjectivity'] = PietSmietStatsSubtitles['subtitles'].apply(subjectivity)
# PietSmietStatsSubtitles['polarity'] = PietSmietStatsSubtitles['subtitles'].apply(polarity)
# PietSmietStatsSubtitles.to_csv('VideoStatisiken/PietSmietPolSubj')

# MaximStatsSubtitles['subjectivity'] = MaximStatsSubtitles['subtitles'].apply(subjectivity)
# MaximStatsSubtitles['polarity'] = MaximStatsSubtitles['subtitles'].apply(polarity)
# MaximStatsSubtitles.to_csv('VideoStatisiken/MaximPolSubj')

# GrummelFritzStatsSubtitles['subjectivity'] = GrummelFritzStatsSubtitles['subtitles'].apply(subjectivity)
# GrummelFritzStatsSubtitles['polarity'] = GrummelFritzStatsSubtitles['subtitles'].apply(polarity)
# GrummelFritzStatsSubtitles.to_csv('VideoStatisiken/GrummelFritzPolSubj')

# BeamStatsSubtitles['subjectivity'] = BeamStatsSubtitles['subtitles'].apply(subjectivity)
# BeamStatsSubtitles['polarity'] = BeamStatsSubtitles['subtitles'].apply(polarity)
# BeamStatsSubtitles.to_csv('VideoStatisiken/BeamPolSubj')

# data['subjectivity'] = data['subtitles'].apply(subjectivity)
# data['polarity'] = data['subtitles'].apply(polarity)
# data.to_pickle("Corpus_Dokument-Term_Matrix/PolSubj.pkl")

HandOfBloodPolSubj = pd.read_csv('VideoStatisiken/HandOfBloodPolSubj')
PietSmietSubtitlesPolSubj = pd.read_csv('VideoStatisiken/PietSmietPolSubj')
MaximPolSubj = pd.read_csv('VideoStatisiken/MaximPolSubj')
GrummelFritzPolSubj = pd.read_csv('VideoStatisiken/GrummelFritzPolSubj')
BeamPolSubj = pd.read_csv('VideoStatisiken/BeamPolSubj')

creator_list = [(HandOfBloodPolSubj, "HandOfBlood"), (PietSmietSubtitlesPolSubj, "PietSmiet"), (MaximPolSubj, "Maxim"),
                (GrummelFritzPolSubj, "GrummelFritz"), (BeamPolSubj, "Beam")]

fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(20, 90), sharey="row")
fig.subplots_adjust(hspace=.8, wspace=.3)
i = 0
for creator in creator_list:
    sns.lineplot(data=creator[0].head(35), ax=axes[0][i], x=creator[0].index[0:35],
                 y=creator[0]["polarity"].head(35)).set(title=creator[1], xlabel="Video", ylabel="Polarität")
    sns.scatterplot(data=creator[0], ax=axes[1][i], x='polarity', y='likeCount').set(title=creator[1],
                                                                                     xlabel="Polarität", ylabel="Likes")
    sns.lineplot(data=creator[0].head(35), ax=axes[2][i], x=creator[0].index[0:35],
                 y=creator[0]["subjectivity"].head(35)).set(title=creator[1], xlabel="Video", ylabel="Subjektivität")
    sns.scatterplot(data=creator[0], ax=axes[3][i], x='polarity', y='commentCount').set(title=creator[1],
                                                                                        xlabel="Polarität",
                                                                                        ylabel="Kommentare")
    i = i + 1
plt.show()


def two_scales(ax1, video, data1, data2, c1, c2):
    ax2 = ax1.twinx()
    ax1.plot(video, data1, color=c1, marker="o")
    ax1.set_xlabel('Video')
    ax1.set_ylabel('Polarität', color=c1)
    ax2.plot(video, data2, color=c2, marker="o")
    ax2.set_ylabel('Likes', color=c2)
    return ax1, ax2


fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(10, 5))
fig.tight_layout()
ax1, ax1a = two_scales(ax1, HandOfBloodPolSubj.index[0:30], HandOfBloodPolSubj["polarity"].head(30), HandOfBloodPolSubj["likeCount"].head(30), 'r', 'b')
ax1.set_title("HandOfBlood")
ax2, ax2a = two_scales(ax2, PietSmietSubtitlesPolSubj.index[0:30], PietSmietSubtitlesPolSubj["polarity"].head(30), PietSmietSubtitlesPolSubj["likeCount"].head(30), 'r', 'b')
ax2.set_title("PietSmiet")
ax3, ax3a = two_scales(ax3, MaximPolSubj.index[0:30], MaximPolSubj["polarity"].head(30), MaximPolSubj["likeCount"].head(30), 'r', 'b')
ax3.set_title("Maxim")
ax4, ax4a = two_scales(ax4, GrummelFritzPolSubj.index[0:30], GrummelFritzPolSubj["polarity"].head(30), GrummelFritzPolSubj["likeCount"].head(30), 'r', 'b')
ax4.set_title("GrummelFritz")
ax5, ax5a = two_scales(ax5, BeamPolSubj.index[0:30], BeamPolSubj["polarity"].head(30), BeamPolSubj["likeCount"].head(30), 'r', 'b')
ax5.set_title("Beam")
plt.show()


plt.rcParams['figure.figsize'] = [10, 8]

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/PolSubj.pkl')

for index, creator in enumerate(data.index):
    x = data.polarity.loc[creator]
    y = data.subjectivity.loc[creator]
    plt.scatter(x, y, color='blue')
    plt.text(x + .001, y - .001, creators[index], fontsize=10)
    plt.xlim(-.2, .5)

# plt.title('Sentiment Analysis', fontsize=20)
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
