import sqlite3
import requests
from datetime import *
import numpy as np
import pandas as pd
from django.db import models

conn = sqlite3.connect(r'Databases/stories.db')
cursor = conn.cursor()

today = datetime.now()
today_date = today.strftime("%Y-%m-%d")
yesterday = today - timedelta(days=1)
yesterday_date = yesterday.strftime("%Y-%m-%d")

query = 'stock market'

dictionary = {}


class Story:
    def __init__(self, articles, sources_bias):
        articles_dict = {}
        source_bias_dict = {"Left": "", "Left Leaning": "", "Center": "", "Right Leaning": "", "Right": ""}
        sources_bias = source_bias_dict
        self.sources_bias = sources_bias
        self.articles = list(articles.values())[2]
        count = 0
        while count <= len(self.articles) - 1:
            dict_key = dict(self.articles[count]).get("source")
            dict_key = dict_key.get("name")
            dict_value = dict(self.articles[count]).get("title")
            articles_dict.__setitem__(dict_key, dict_value)
            count += 1

        self.articles = articles_dict

    def dictionary_pass(self):
        articles_dict = self.articles
        return articles_dict

    def to_df(self):
        story_frame = pd.DataFrame({"skew": list(self.sources_bias.values())}, index=list(self.sources_bias.keys()))
        print(story_frame)
        return story_frame


def query_string_db_format(str):
    query_new = str.replace(" ", "_")
    print(query_new)
    return query_new


def dynamic_request(string):
    url = (f'https://newsapi.org/v2/everything?q={string}&from={yesterday_date}&to={today_date}'
           f'&sortBy=relevancy&language=en&apiKey'
           f'=e1314804b13e41a3af10a6f9ebb352de')

    response = requests.get(url)
    return response.json()


def story_inst_struct(model, dictionary):
    query = model.query
    query_check = 0
    if len(dictionary.keys()) < 1:
        pass
    else:
        for key in dictionary.keys():
            for char in query:
                if key.find(char) == char:
                    query_check += 1
            if query_check == len(str(key)):
                raise Exception("You've already searched for this topic, please try another")
            else:
                pass
    user_request = dynamic_request(query)
    dictionary.update({query: [Story(user_request, ''), model]})







