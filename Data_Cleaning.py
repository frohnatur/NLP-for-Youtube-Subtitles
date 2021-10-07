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

for i in range(1, 41):
    with open("HandOfBloodSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    HandOfBloodSubtitles += text

for i in range(1, 112):
    with open("PietSmietSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    PietSmietSubtitles += text

for i in range(1, 46):
    with open("MaximSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    MaximSubtitles += text

for i in range(1, 24):
    with open("GrummelFritzSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    GrummelFritzSubtitles += text

data = {"HandOfBlood": HandOfBloodSubtitles, "PietSmiet": PietSmietSubtitles, "Maxim": MaximSubtitles,
        "GrummelFritz": GrummelFritzSubtitles}
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

