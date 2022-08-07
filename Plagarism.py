import os
import numpy as np
import sklearn
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from numpy import dot
from numpy.linalg import norm
# folder path
dir_path = r'/Users/anuhyakalvakala/Desktop/ML'

# list to store files
document_list = []

def normalize_doc(doc):    
    doc =  re.sub('[^a-zA-Z0-9\n\.]', ' ', doc)
    doc = doc.lower()
    doc = doc.strip()
# convert the sring into lower
    tokens = wpt.tokenize(doc)  
    print(tokens)
# filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
# re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    print(doc)
    return doc

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if path.endswith(".txt"):
        document_list.append(path)
print(document_list)
doc_values =[open(doc, encoding = "ISO-8859-1").read() for doc in  document_list]
corpus =np.array(doc_values)
corpus_df = pd.DataFrame({'Document': corpus})
corpus_df
print(corpus)
wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')
 
normalize_corpus = np.vectorize(normalize_doc)
print(normalize_corpus)
norm_corpus = normalize_corpus(corpus)
print(norm_corpus)
cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(norm_corpus)
cv_matrix = cv_matrix.toarray()
cv_matrix
# get all unique words in the corpus
vocab = cv.get_feature_names()
# show document feature vectors
pd.DataFrame(cv_matrix, columns=vocab)

for i in range(len(cv_matrix)):
    print("#############################")
    for j in range(0, len(cv_matrix)):
        result = dot(cv_matrix[i], cv_matrix[j])/(norm(cv_matrix[i])*norm(cv_matrix[j]))
        print(result)

#for doc in corpus:
 #   normalize_doc(doc)