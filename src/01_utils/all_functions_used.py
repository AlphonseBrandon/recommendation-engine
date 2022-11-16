'''
Author: Alphonse Brandon
Last Updated Date: 11/16/2022
Last Updated Time: 8:53 PM

Description: This script contains all the function used in building my content based filtering recommendation system
'''

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import bs4 as bs
import urllib.request
import pickle
import requests

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



load_the_movie_dataset()
remove_nul_values_from_data()
create_clean_data()
save_cleaned_data()