'''
Author: Alphonse Brandon
Last Updated Date: 11/16/2022
Last Updated Time: 10:29 PM

Description: This script contains all the function used in building my content based filtering recommendation system
'''

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests

'''########===== This first batch of functions are used to cleaning the data =====######'''

def load_the_movie_dataset():
    '''This function loads the movie dataset'''
    global data
    
    data_path = 'D:/github-repos/ml-based-recommendation-engine-project/data/01_raw/movies_up_to_2018.csv'
    data = pd.read_csv(data_path)  


def remove_nul_values_from_data():
    '''This function cleans the dataset by removing all null values'''
    global data
    data = data.dropna(how='any', axis=0)
    return data

def create_clean_data():
    '''This function creates the cleaned dataset'''
    global cleaned_data
    cleaned_data = remove_nul_values_from_data()
    return cleaned_data

def save_cleaned_data():
    '''This function saves the cleaned dataset to the data/02_intermediate directory'''
    global cleaned_data
    path_to_cleaned_data = 'D:/github-repos/ml-based-recommendation-engine-project/data/02_intermediate/movies_data.csv'
    
    cleaned_data.to_csv(path_to_cleaned_data, index=False)


'''########===== This next batch of functions are used for building the recommendation engine =====######'''

def load_cleaned_data():
    '''This function loads the cleaned data'''
    global data
    path_to_data = 'D:/github-repos/ml-based-recommendation-engine-project/data/02_intermediate/movies_data.csv'
    data = pd.read_csv(path_to_data)
    
def create_a_count_matrix(data):
    '''This function converts the data into numerical matrices'''
    global count_matrix, cv
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])


def create_similarity_score_matrix():
    '''This function computes the similarity score between movies'''
    global similarity
    similarity = cosine_similarity(count_matrix)
    

def checking_if_similarity_has_been_created():
    '''This function checks if the similary score has been created'''
    global similarity, data
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity_score_matrix(data=data)

def make_movie_title_lowercase(movie_title):
    '''This function renders the movie title in lowercase
    :param: the movie title to get similar movies'''
    return movie_title.lower()


def get_list_of_simirlar_movies(movie_title):
    '''This function fetches similar movies from our data file
    :param: the movie title of the movie we want to get simirlar movies to it'''
    global similarity
    if movie_title not in data['movie_title'].unique():
        return ('Oh no! the movie you requested is not in our database yet. Please check the spelling or try another movie title')
    else:
        movie_index = data.loc[data['movie_title']==movie_title].index[0]
        list_of_movies = list(enumerate(similarity[movie_index]))
        sorted_list_of_movies = sorted(list_of_movies, key=lambda x:x[1], reverse=True)
        top_four_similar_movies = sorted_list_of_movies[1:5]
        recommended_movies_list = []
        for movie in range(len(top_four_similar_movies)):
            recommended_movie = top_four_similar_movies[movie][0]
            recommended_movies_list.append(data['movie_title'][recommended_movie])
        
        return recommended_movies_list


def recommend_movies(movie_title):
    '''This function recommends similar movies
    :param: movie title from frontend input'''

    global similarity
    movie_title = make_movie_title_lowercase(movie_title)
    checking_if_similarity_has_been_created()
    return get_list_of_simirlar_movies(movie_title)

