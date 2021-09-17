import pandas as pd

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix.pkl')
data = data.transpose()
print(data.head())

top_dict = {}
for column in data.columns:
    top = data[column].sort_values(ascending=False).head(30)
    top_dict[column] = list(zip(top.index, top.values))

for creator, top_words in top_dict.items():
    print(creator)
    print(', '.join([word for word, count in top_words[0:29]]))
    print('---')