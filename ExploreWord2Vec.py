"""Playing with word2vec model"""
import sys
import csv

#%%
from gensim.models import Word2Vec

year=sys.argv[1]
model = Word2Vec.load(f"venv/{year}_sents.model")
print(model.wv.most_similar("agricultural", topn=5))
#print(model.wv['trade'])

#vocab1=list(model.wv.vocab)
#[vocab1] avoid comma between each characters
#with open(f'/home/myriam/modNum/data/csv/{year}vocab.csv','w') as f:
 #   w = csv.writer(f)
  #  w.writerows([vocab1]) 
   # f.close

"""agricultural=model.wv.most_similar("agricultural", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}agricultural.csv','w') as f:
    w = csv.writer(f)
    w.writerows(agricultural) 
    f.close
market=model.wv.most_similar("market",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}market.csv','w') as f:
    w = csv.writer(f)
    w.writerows(market) 
    f.close
wine=model.wv.most_similar("wine", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}wine.csv','w') as f:
    w = csv.writer(f)
    w.writerows(wine) 
    f.close
fish=model.wv.most_similar("fish",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}fish.csv','w') as f:
    w = csv.writer(f)
    w.writerows(fish) 
    f.close

adherence=model.wv.most_similar("adherence", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}adherence.csv','w') as f:
    w = csv.writer(f)
    w.writerows(adherence) 
    f.close

deliberation=model.wv.most_similar("deliberation", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}deliberation.csv','w') as f:
    w = csv.writer(f)
    w.writerows(deliberation) 
    f.close
    
member=model.wv.most_similar("member", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}member.csv','w') as f:
    w = csv.writer(f)
    w.writerows(member) 
    f.close
economic=model.wv.most_similar("economic",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}economic.csv','w') as f:
    w = csv.writer(f)
    w.writerows(economic) 
    f.close
employment=model.wv.most_similar("employment", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}employmentl.csv','w') as f:
    w = csv.writer(f)
    w.writerows(employment) 
    f.close
energy=model.wv.most_similar("energy",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}energy.csv','w') as f:
    w = csv.writer(f)
    w.writerows(energy) 
    f.close
coal=model.wv.most_similar("coal", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}coal.csv','w') as f:
    w = csv.writer(f)
    w.writerows(coal) 
    f.close
steel=model.wv.most_similar("steel",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}steel.csv','w') as f:
    w = csv.writer(f)
    w.writerows(steel) 
    f.close
transport=model.wv.most_similar("transport", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}transport.csv','w') as f:
    w = csv.writer(f)
    w.writerows(transport) 
    f.close
meat=model.wv.most_similar("meat",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}meat.csv','w') as f:
    w = csv.writer(f)
    w.writerows(meat) 
    f.close
research=model.wv.most_similar("research", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}research.csv','w') as f:
    w = csv.writer(f)
    w.writerows(research) 
    f.close
textile=model.wv.most_similar("textile",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}textile.csv','w') as f:
    w = csv.writer(f)
    w.writerows(textile) 
    f.close
cotton=model.wv.most_similar("cotton", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}cotton.csv','w') as f:
    w = csv.writer(f)
    w.writerows(cotton) 
    f.close
imports=model.wv.most_similar("imports",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}imports.csv','w') as f:
    w = csv.writer(f)
    w.writerows(imports) 
    f.close
trade=model.wv.most_similar("trade", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}trade.csv','w') as f:
    w = csv.writer(f)
    w.writerows(trade) 
    f.close
treaty=model.wv.most_similar("treaty",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}treaty.csv','w') as f:
    w = csv.writer(f)
    w.writerows(treaty) 
    f.close
milk=model.wv.most_similar("milk", topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}milk.csv','w') as f:
    w = csv.writer(f)
    w.writerows(milk) 
    f.close
quota=model.wv.most_similar("quota",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}quota.csv','w') as f:
    w = csv.writer(f)
    w.writerows(quota) 
    f.close
custom=model.wv.most_similar("custom",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}custom.csv','w') as f:
    w = csv.writer(f)
    w.writerows(custom) 
    f.close
tariff=model.wv.most_similar("tariff",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}tariff.csv','w') as f:
    w = csv.writer(f)
    w.writerows(tariff) 
    f.close
electricity=model.wv.most_similar("electricity",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}electricity.csv','w') as f:
    w = csv.writer(f)
    w.writerows(electricity) 
    f.close
workers=model.wv.most_similar("workers",topn=15)
with open(f'/home/myriam/modNum/data/csv/{year}workers.csv','w') as f:
    w = csv.writer(f)
    w.writerows(workers) 
    f.close"""

#%%
#pprint(model.wv.most_similar(positive=['workshops', 'economics'], negative=['success'],topn=20))


