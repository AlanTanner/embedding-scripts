import helpers.cleaning_helpers as ch
import os

def main():
    for filename in os.listdir('data/raw'):
        with open('data/raw/' + filename, 'r') as f:
            raw_text = f.read()
    #if .md file use clean_md, else use clean_text
            if filename.split('.')[1] == 'md':
                cleaned_text = ch.clean_md(raw_text)
            else:
                cleaned_text = ch.clean_text(raw_text)
    #write cleaned text to new file
            with open('data/cleaned/' + filename.split('.')[0] + '.cleaned', 'w') as f:
                f.write(cleaned_text)