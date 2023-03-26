import os
import json
import helpers.embedding_helpers as eh

def main():
    for filename in os.listdir('data/cleaned'):
        with open('data/cleaned/' + filename, 'r') as f:
            cleaned_text = f.read()

            #embed text
            embeds = eh.embed_text(cleaned_text)
            
            #write embedding to a file as json
            with open('data/embedding/' + filename.split('.')[0] + '.embedding', 'w') as f:
                json.dump(embeds, f)
