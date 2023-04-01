import os
import helpers.index_helpers as ih
import json

#load in data/embedding files into a tuple of string and list of embeddings
#each tuple is a file
#each embedding is a list of 512 floats
embeddings = []
for filename in os.listdir('data/embedding/'):
    with open('data/embedding/' + filename, 'r') as e:
            embeddings.append((filename.split('.')[0], json.load(e)))

#print the first tuples list of embeddings
#print(len(embeddings[0][0]))
#index embeddings with pinecone
ih.index_embeddings(embeddings)
