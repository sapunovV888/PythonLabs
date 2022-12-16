import nltk
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import string


tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
text = open('chesterton-ball.txt', 'r', encoding='utf-8').read()
tokens = tokenizer.tokenize(text)
print('all words in text = ', len(tokens))
all_words_dist = nltk.FreqDist(w.lower() for w in tokens)
mostCommon = all_words_dist.most_common(10)
print('TOP 10 WORDS WITH STOPWORDS\n',pd.DataFrame(mostCommon, columns=['Word','Repeat in text']))
plt.figure(1)
plt.subplots_adjust(hspace=0.5)
plt.subplot(211)
plt.bar([i[0] for i in mostCommon], [i[1] for i in mostCommon], width=0.5, color='blue')
plt.xlabel('Word')
plt.ylabel('Value of numbers this word in text')
plt.title('Top 10 words with stopwords')
stopwords = nltk.corpus.stopwords.words("english")
all_words_without_SW_dist = nltk.FreqDist(w.lower() for w in tokens if w not in stopwords)
mostCommon = all_words_without_SW_dist.most_common(10)
print('TOP 10 WORDS WITHOUT STOPWORDS\n',pd.DataFrame(mostCommon, columns=['Word','Repeat in text']))
plt.subplot(212)
plt.bar([i[0] for i in mostCommon], [i[1] for i in mostCommon], width=0.5, color='yellow')
plt.xlabel('Word')
plt.ylabel('Value of numbers this word in text')
plt.title('Top 10 words without stopwords')
plt.show()

