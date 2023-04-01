import os
import pinecone
import openai
import json

MODEL = "text-embedding-ada-002"

#initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV") # find next to API key in console
)

#connect to index already created in pinecone
indexstring = os.getenv("PINECONE_INDEX")
index = pinecone.Index(indexstring)

openai.organization = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

# create function that takes in a string and returns a list of embeddings
query = ""

xq = openai.Embedding.create(input=query, engine=MODEL)['data'][0]['embedding']

res = index.query([xq], top_k=5, include_metadata=False)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['id']}")