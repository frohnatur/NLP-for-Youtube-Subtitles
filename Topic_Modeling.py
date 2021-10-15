import pandas as pd
import pickle
from gensim import matutils, models
import scipy.sparse
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_pickle('Corpus_Dokument-Term_Matrix/Dokument-Term-Matrix_Total_StopWords.pkl')
tdm = data.transpose()

corpus = matutils.Sparse2Corpus(scipy.sparse.csr_matrix(tdm))

cv = pickle.load(open("Corpus_Dokument-Term_Matrix/Count_Vektorizer_Total_Stopwords.pkl", "rb"))
id2word = dict((v, k) for k, v in cv.vocabulary_.items())

lda = models.LdaModel(corpus=corpus, id2word=id2word, num_topics=2, passes=10)
#print(lda.print_topics())


# Nur Substantive und Adjektive

data_clean = pd.read_pickle('Corpus_Dokument-Term_Matrix/Corpus.pkl')

stopwords = stopwords.words("german")
add_stopwords = ['ja', 'mal', 'okay', 'glaube', 'schon', 'gut', 'einfach', 'immer', 'geht', 'halt', 'mehr', 'bisschen', 'ganz', 'gar', 'weiß', 'kommt', 'vielleicht', 'macht', 'wahrscheinlich', 'ok', 'gerade', 'gibt', 'wirklich', 'gehen', 'kommen', 'sagen', 'zwei', 'erst', 'eigentlich', 'natürlich', 'oben', 'irgendwie', 'hoch', 'müssen', 'fall']
stop_words = list(set(add_stopwords + stopwords))

def nouns_adj(text):
    is_noun_adj = lambda pos: pos[:2] == 'NN' or pos[:2] == 'JJ'
    tokenized = word_tokenize(text)
    nouns_adj = [word for (word, pos) in pos_tag(tokenized) if is_noun_adj(pos)]
    return ' '.join(nouns_adj)

data_nouns_adj = pd.DataFrame(data_clean.subtitles.apply(nouns_adj))

cvna = CountVectorizer(stop_words=stop_words, max_df=.8)
data_cvna = cvna.fit_transform(data_nouns_adj.subtitles)
data_dtmna = pd.DataFrame(data_cvna.toarray(), columns=cvna.get_feature_names())
data_dtmna.index = data_nouns_adj.index

corpusna = matutils.Sparse2Corpus(scipy.sparse.csr_matrix(data_dtmna.transpose()))

id2wordna = dict((v, k) for k, v in cvna.vocabulary_.items())

ldana = models.LdaModel(corpus=corpusna, num_topics=4, id2word=id2wordna, passes=80)
print(ldana.print_topics()[0])
print(ldana.print_topics()[1])
print(ldana.print_topics()[2])
print(ldana.print_topics()[3])

corpus_transformed = ldana[corpusna]
print(list(zip([a for [(a,b)] in corpus_transformed], data_dtmna.index)))