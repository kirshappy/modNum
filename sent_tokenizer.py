"""Tokenize sentences"""

import os
import sys
import nltk
from nltk.tokenize import sent_tokenize
"""nltk.download('punkt')"""

nltk.data.path.append("/srv/resources/nltk_data/")

year = sys.argv[1]
infile = f"data/txt/{year}.tsv"
if not os.path.isfile(infile):
    infile = f"data/txt/{year}.txt"
outfile = f"data/txt/{year}_sents.txt"

with open(outfile, 'w', encoding="utf-8") as output:
    with open(infile, encoding="utf-8", errors="backslashreplace") as f:
        for line in f:
            elems = line.strip().split("\t")
            for elem in elems:
                sentences = sent_tokenize(elem)
                for sent in sentences:
                    output.write(sent + "\n")