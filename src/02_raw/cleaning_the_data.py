'''
Author: Alphonse Brandon
Last Updated Date: 11/16/2022
Last Updated Time: 10:22 PM

Description: This script contains all the function used in building my content based filtering recommendation system
'''

import sys

sys.path.insert(1, 'D:/github-repos/ml-based-recommendation-engine-project/src/01_utils')

import all_functions_used

all_functions_used.load_the_movie_dataset()
all_functions_used.remove_nul_values_from_data()
all_functions_used.create_clean_data()
all_functions_used.save_cleaned_data()
