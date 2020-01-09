import logging
import sys

from gensim.models.phrases import Phrases, Phraser
from gensim.models.word2vec import Word2Vec

import nltk
#from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize

year = sys.argv[1]
#wnl=WordNetLemmatizer()
nltk.data.path.append("/home/myriam/nltk_data")

logging.basicConfig(format='%(asctime)s:%(threadName)s:%(levelname)s:%(message)s',level=logging.INFO)

class MySentences(object):
    def __init__(self,filename):
        self.filename=filename

    def __iter__(self):
        for line in open(self.filename,encoding='utf-8',errors="backslashreplace"):
            yield[w.lower() for w in wordpunct_tokenize(line)]

infile=f"data/txt/{year}_sents.txt"
sentences=MySentences(infile)
phrases=Phrases(sentences)
bigram=Phraser(phrases)
trigram=Phrases(bigram[sentences])
quadrigram=Phrases(trigram[bigram[sentences]])
corpus=list(quadrigram[trigram[bigram[sentences]]])
#model=Word2Vec(corpus,size=32,window=5,min_count=500,workers=4,iter=5)
model=Word2Vec(corpus,size=32,window=5,min_count=200,workers=4,iter=5)
outfile=f"venv/{year}_sents200.model"
model.save(outfile)