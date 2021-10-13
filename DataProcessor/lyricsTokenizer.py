import nltk
from nltk.corpus import stopwords
from nltk.stem import wordnet
from nltk.tokenize import word_tokenize
from wordLemmatizer import POSTagger
import re

def wordLemmatizer(word):
    lemmatizer = wordnet.WordNetLemmatizer()
    s = nltk.pos_tag([word])[0][1]
    return lemmatizer.lemmatize(word,POSTagger(s))


def tokenizer(lyric):
    stop_words = set(stopwords.words('english'))
    tokenizedLyrics = []
    split_lyrics = lyric.split("\n")
    

    for i in range(0,len(split_lyrics)):
        word_tokens = word_tokenize(split_lyrics[i])        
        filtered_lyrics = []
        
        for w in word_tokens:
            if w.lower() not in stop_words and (w != ',' and not re.search("[@_!#$%^&*()<>?/|}{~:'.;,\-]",w) and len(w) > 1): 
                w = w.lower()
                filtered_lyrics.append(wordLemmatizer(w))
        
        if len(filtered_lyrics) != 0:
            tokenizedLyrics.append(filtered_lyrics)
    return tokenizedLyrics
    
