import nltk
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import string

nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
text = open('data.txt', 'r', encoding='utf-8').read()
tokens = tokenizer.tokenize(text)
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n',text,'\n')
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT TOKENIZATION IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n',tokens,'\n')
wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()
WL = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT LEMMATIZATION IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n', WL, '\n')
ps = nltk.PorterStemmer()
PS = [ps.stem(t) for t in tokens]
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT STEMMING IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n', PS, '\n')
stopwords = nltk.corpus.stopwords.words("english")
all_text_without_SW_dist = [word for word in tokens if word not in stopwords]
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT WITHOUT STOP WORDS IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n', all_text_without_SW_dist, '\n')
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
PN = tokenizer.tokenize(' '.join(tokens))
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/~~~~OUR TEXT WITHOUT PUNCTUATION IS~~~~\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n', PN, '\n')