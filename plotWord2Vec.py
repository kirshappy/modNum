"""Plot word2vec model Vocabulary"""
import sys
import csv
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

from gensim.models import Word2Vec
from pprint import pprint

year=sys.argv[1]
model = Word2Vec.load(f"venv/{year}_sents200.model")

def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        #annotate dot with label
        """plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')"""
    plt.suptitle(f'Vocabulary Representation for {year}')
    plt.show()

tsne_plot(model)
#plot 2code source https://www.kaggle.com/jeffd23/visualizing-word-vectors-with-t-sne