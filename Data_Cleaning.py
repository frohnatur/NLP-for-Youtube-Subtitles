import pandas as pd
import re
import string

HandOfBloodSubtitles = ""
PietSmietSubtitles = ""

for i in range(1,41):
    with open("HandOfBloodSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    HandOfBloodSubtitles += text

for i in range(1,112):
    with open("PietSmietSubtitles/video" + str(i) + ".txt", encoding="utf-8") as file:
        text = file.read()
    PietSmietSubtitles += text

data = {"HandOfBlood" : HandOfBloodSubtitles, "PietSmiet" : PietSmietSubtitles}
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

cleaning = lambda x: clean_text(x)

data_clean = pd.DataFrame(data.subtitles.apply(cleaning))
data_clean

with open('test4.txt', 'w', encoding='utf-8') as file:
    file.write(data_clean.iloc[0,0])

print(data)
print(data_clean)

