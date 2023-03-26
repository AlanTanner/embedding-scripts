import os
import openai

MODEL = "text-embedding-ada-002"

openai.organization = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

# create function that takes in a string and returns a list of embeddings
def embed_text(text):
    res = openai.Embedding.create(
        input=[
            text
        ], engine="text-embedding-ada-002"
    )
    embeds = [record['embedding'] for record in res['data']]
    return embeds