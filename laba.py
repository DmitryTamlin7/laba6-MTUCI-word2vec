from pymystem3 import Mystem
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import pandas as pd
import re
import word2vec 
import gensim



"""
df = pd.read_csv('Master_and_Margarita_19.csv', sep=';')
df = df.dropna()

file = open('Master_and_Margarita_19.txt', 'w')

for text in df['Message']:
    text = text.lover()


    res = re.findall('[а-яё]+', text)
    for i in res:
        file.write(i)
        file.write(' ')
    file.write('.')
file.close()

# Убураем ненужные значения, переводим в ниж регистр и убираем числа(re)
# отделяем слова пробелом а файлы точкой
"""

"""
file = open('Master_and_Margarita_19.txt')
text = file.read()
posts = text.split(".")
m = Mystem

with open('Master_and_Margarita_19_lemma.txt', "w") as output_file:
    for post in posts:
        output_file.write("".join(m.lemmatize(post)))




word2vec.word2phrase('Master_and_Margarita_19_lemma.txt', 
                     'Master_and_Margarita_19_lemma.txt-phrases', verbose= True)

word2vec.word2vec('Master_and_Margarita_19_lemma.txt-phrases',
                  'Master_and_Margarita_19_lemma.txt-bin', verbose= True)
"""
# word2vec.word2phrase('Master_and_Margarita_19_lemma.txt', 
#                      'Master_and_Margarita_19_lemma.txt-phrases', verbose= True)
# word2vec.word2phrase('text8', 
#                      'text8-ph', verbose= True)

word2vec.word2vec('text8',
                  'text8-w2v', verbose= True)

# model = gensim.models.KeyedVectors.load_word2vec_format('Master_and_Margarita_19_lemma.txt-bin', binary= False)

# file = open('slovo_Margarita.txt', 'w')

# for i in model.most_similar(positive = ['маргарита'], topn = 10):

#     file.write(str(i))
#     file.write('\n')

# file.close()