import os
import pinecone



##create a function to index the embeddings
def index_embeddings(embeds):
# initialize connection to pinecone (get API key at app.pinecone.io)
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV") # find next to API key in console
    )

    # connect to index already created in pinecone
    indexstring = os.getenv("PINECONE_INDEX")
    index = pinecone.Index(indexstring)
    print(len(embeds))
    ##loop through each tuple in embeds
    for i in range(len(embeds)):
            #add each embedding to the index
            to_upsert = zip(embeds[i][0],list(embeds[i][1]))
            index.upsert(vectors=list(to_upsert))