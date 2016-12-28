import pandas as pd
import numpy as np

data = pd.read_csv('Data.csv')
data = data.dropna() 
data = data[['movie_title', 'director_name', 'title_year','country', 'budget']]
data['title_year'] = data['title_year'].apply(int)
data['budget'] = data['budget'].apply(int)
data['director_first_name'], data['director_last_name'] = data['director_name'].str.split(' ', 1).str
data = data.drop('director_name', 1)
data.to_csv('preprocessing.csv')
