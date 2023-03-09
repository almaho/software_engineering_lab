import scrapy


class IsnaSpider(scrapy.Spider):
    name = 'Isna'
    allowed_domains = ['www.isna.ir']
    start_urls = ['http://www.isna.ir/']

    def parse(self, response):
        pass
from hazm import *
import numpy as np
import itertools
import numpy as np
import pandas as pd

import networkx as nx
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

news1 = pd.read_csv('newsrecent.csv')
news2 = pd.read_csv('newslast.csv')
all_news = [news1]
all_strings = []
for news in all_news :
#     string = ''
    for i in range(500) :
        string = news.loc[i]['body']
        all_strings.append(string)
# normalizer = Normalizer()
# n = len(all_strings) 
# for i in range(n) :
#     all_strings[i] = normalizer.normalize(all_strings[i])
    
# paragraphs = []
# for string in all_strings :
#     word = []
#     for x in sent_tokenize(string) :    
#         for a in word_tokenize(x) :
#             word.append(a)
#     paragraphs.append(word)
# stemmer = Stemmer()
# for i in range(n) :
#     paragraphs[i] = [stemmer.stem(word) for word in paragraphs[i]]
# lemmatizer = Lemmatizer()
# for i in range(n) :
#     paragraphs[i] = [lemmatizer.lemmatize(stem) for stem in paragraphs[i]]

