import pandas as pd
import re
import string
import pickle
# import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

HandOfBloodSubtitles = ""
PietSmietSubtitles = ""
MaximSubtitles = ""
GrummelFritzSubtitles = ""
BeamSubtitles = ""

HandofBloodStats = pd.read_csv('VideoStatisiken/HandOfBlood', index_col=0)
PietSmietStats = pd.read_csv('VideoStatisiken/PietSmiet', index_col=0)
MaximStats = pd.read_csv('VideoStatisiken/Maxim', index_col=0)
GrummelFritzStats = pd.read_csv('VideoStatisiken/GrummelFritz', index_col=0)
BeamStats = pd.read_csv('VideoStatisiken/Beam', index_col=0)

for i in range(0, 41):
    with open("HandOfBloodSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    HandofBloodStats.at[i, "subtitles"] = text
    HandOfBloodSubtitles += text

for i in range(0, 114):
    with open("PietSmietSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    PietSmietStats.at[i, "subtitles"] = text
    if text != 'NoSubtitles':
        PietSmietSubtitles += text

for i in range(0, 45):
    with open("MaximSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    MaximStats.at[i, "subtitles"] = text
    MaximSubtitles += text

for i in range(0, 36):
    with open("GrummelFritzSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    GrummelFritzStats.at[i, "subtitles"] = text
    if text != 'NoSubtitles':
        GrummelFritzSubtitles += text

for i in range(0, 123):
    with open("BeamSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    BeamStats.at[i, "subtitles"] = text
    if text != 'NoSubtitles':
        BeamSubtitles += text

data = {"HandOfBlood": HandOfBloodSubtitles, "PietSmiet": PietSmietSubtitles, "Maxim": MaximSubtitles,
        "GrummelFritz": GrummelFritzSubtitles, "Beam" : BeamSubtitles}
data = pd.DataFrame.from_dict(data, orient="index")
data.columns = ["subtitles"]


def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    text = text.strip()
    return text

data_clean = pd.DataFrame(data.subtitles.apply(lambda x: clean_text(x)))

HandofBloodStats["subtitles"] = HandofBloodStats["subtitles"].apply(lambda x: clean_text(x))
HandofBloodStats.to_csv('VideoStatisiken/HandOfBloodStatsSubtitles')

PietSmietStats.drop(PietSmietStats[PietSmietStats["subtitles"] == "NoSubtitles"].index, inplace=True)
PietSmietStats.reset_index(inplace=True, drop=True)
PietSmietStats["subtitles"] = PietSmietStats["subtitles"].apply(lambda x: clean_text(x))
PietSmietStats.to_csv('VideoStatisiken/PietSmietStatsSubtitles')

MaximStats["subtitles"] = MaximStats["subtitles"].apply(lambda x: clean_text(x))
MaximStats.to_csv('VideoStatisiken/MaximStatsSubtitles')

GrummelFritzStats.drop(GrummelFritzStats[GrummelFritzStats["subtitles"] == "NoSubtitles"].index, inplace=True)
GrummelFritzStats.reset_index(inplace=True, drop=True)
GrummelFritzStats["subtitles"] = GrummelFritzStats["subtitles"].apply(lambda x: clean_text(x))
GrummelFritzStats.to_csv('VideoStatisiken/GrummelFritzStatsSubtitles')

BeamStats.drop(BeamStats[BeamStats["subtitles"] == "NoSubtitles"].index, inplace=True)
BeamStats.reset_index(inplace=True, drop=True)
BeamStats["subtitles"] = BeamStats["subtitles"].apply(lambda x: clean_text(x))
BeamStats.to_csv('VideoStatisiken/BeamStatsSubtitles')

with open('test4.txt', 'w', encoding='utf-8') as file:
    file.write(data_clean.iloc[0, 0])

print(data)
print(data_clean)

# nltk.download('stopwords')
german_stop_words = stopwords.words('german')

cv = CountVectorizer(stop_words=german_stop_words)
data_cv = cv.fit_transform(data_clean.subtitles)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index

print(data_dtm)

data_clean.to_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')
data_dtm.to_pickle("Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix.pkl")
pickle.dump(cv, open("Corpus_Dokument-Term_Matrix/Count_Vektorizer.pkl", "wb"))

