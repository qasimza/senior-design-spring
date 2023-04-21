"""
The following Kaggle Datasets were utilized to create the training dataset:
dataset.csv - https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset?select=dataset.csv
tracks.csv - https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=tracks.csv
data.csv - https://www.kaggle.com/datasets/ektanegi/spotifydata-19212020?resource=download
"""

import pandas as pd

data_set = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                       r'Design\ml_code\data\archive\dataset.csv').drop_duplicates().dropna()

# extract id, release_date from tracks.csv
tracks = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                     r'Design\ml_code\data\archive\tracks.csv')[["id", "release_date"]].drop_duplicates().dropna()

# get column of years
tracks['year'] = tracks['release_date'].str[:4].astype(int)

tracks = tracks.drop('release_date', axis=1)  # drop release date
data_set = data_set.join(tracks.set_index('id'), on='id')  # append years from tracks to data_set based on id

# get id and year from data.csv
data = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                   r'Design\ml_code\data\archive\data.csv')[["id", "year"]].drop_duplicates().dropna()

# append years from data to data_set based on id
data_set = data_set.fillna(data)
data_set = data_set.drop('i', axis=1)
data_set['track_name'] = data_set['track_name'].str.upper()

data_set.to_csv(
    r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior Design\ml_code\data\data_set.csv',
    index=False)  # save cleaned data

# Cleaning artist data
artists_data_set = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                               r'Design\ml_code\data\archive\artists.csv')
artists_data_set.drop(artists_data_set.loc[artists_data_set['genres'] == '[]'].index, inplace=True)
artists_data_set.to_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                        r'Design\ml_code\data\archive\artists_cleaned.csv')
