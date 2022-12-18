import re
import nltk
import gensim 
import pandas as pd
from gensim.models.ldamulticore import LdaMulticore
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

lemmatizer = WordNetLemmatizer()

def clean_text(lst):
    cleaned_text = []
    stopword = stopwords.words("english")
    
    # Очистка тексту від зайвого: проводимо видалення пунктуації, стопслів, пророблюємо процес токенізації та лематизацію 
    for text in lst:
        text = str(text).lower()
        text = re.sub(r'[^\w ]+', "", text)
        text = " ".join([lemmatizer.lemmatize(word,pos='v') for word in word_tokenize(text) if not word in set(stopword) and len(word)>3])
        cleaned_text.append(text)
    return cleaned_text # повертаємо очищений текст
  
    # Створення біграми, біаграма - це послідовність двох суміжних слів із рядка, які з'єднуються для створення більш зрозумілого словосполучення
def make_biagram(data,tokens):
    bigram = gensim.models.Phrases(data, min_count=5, threshold=100) # higher threshold fewer phrases.
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return [bigram_mod[doc] for doc in tokens]  
 

def topic_modeling(data, topic_num):
    #Токенізація
    tokens = []
    for text in data:
        text = word_tokenize(text)
        tokens.append(text)
        
    # Створення біграми
    tokens = make_biagram(data=data,tokens=tokens)

    # Створення корпусу даних після біограми та токенізації
    dictionary = corpora.Dictionary(tokens)
    
    # створення мішка слів за допомогою функції doc2bow
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in tokens]

    ### Створення та тренування LDA моделі 
    lda_model =  gensim.models.LdaModel(doc_term_matrix,   ##   документ мішка слів
                                       num_topics = topic_num,     ## Кількість варіацій тем, що ми бажаємо отримати
                                       id2word = dictionary,     ## Словник частот слів                             
                                       passes = 10,        ## кількість проходів навчання 
                                       chunksize=10,       ## кількість документів яка буде використана у кожному чанку під час навчання
                                       update_every=1,     ## кількість документів для кожного оновлення
                                       alpha='auto',       ## Кількість очікуваних тем
                                       per_word_topics=True,
                                       random_state=0)
                                      
    ### вивід загальних слів для кожної теми з їхніми спорідненими та спільнокореневими словами
    for_wordcloud=''
    for idx, topic in lda_model.print_topics():
        print("Topic: {} \nWords: {}".format(idx, topic ))
        print("\n")
        for_wordcloud=for_wordcloud + str(topic) # запис основних слів теми в рядок для подальшого створення хмари слів
    return for_wordcloud


def generate_wordcloud(text): # optionally add: stopwords=STOPWORDS and change the arg below
    wordcloud = WordCloud(
                          width=800, height=400,
                          relative_scaling = 1.0,
                          stopwords = STOPWORDS # set or space-separated string
                          ).generate(text)
    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


try:
    df = pd.read_csv('data1.csv') 
    df = df.sample(10000)
    headlines = df['headline_text'].to_list()
    #text = headlines[0]
    topic_num=input('please input number of topic variant that you wanna get\n')
    print('please wait a few second for get the most suitable topics for this document\n')
    cleaned_reviews = clean_text(headlines)
    print('-----------the most suitable topics for this document are----------\n')
    tm=topic_modeling(cleaned_reviews,topic_num)
    generate_wordcloud(tm)
except:
    print('file wasn`t found')



