'''
Author: Alphonse Brandon
Last Updated Date: 11/16/2022
Last Updated Time: 10:42 PM

Description: This script contains all the function used in building my content based filtering recommendation system
'''

import sys

sys.path.insert(1, 'D:/github-repos/ml-based-recommendation-engine-project/src/01_utils')

import all_functions_used


all_functions_used.load_cleaned_data()
all_functions_used.create_a_count_matrix()
all_functions_used.create_similarity_score_matrix()
all_functions_used.checking_if_similarity_has_been_created()
all_functions_used.recommend_movies('Avatar')
