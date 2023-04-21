from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Load artist dataframe
artists_data_set = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                               r'Design\ml_code\data\archive\artists_cleaned_genres.csv')

artists_data_set.drop(artists_data_set.loc[artists_data_set['popularity'] == 0].index, inplace=True)

artists_data_set.drop(artists_data_set.loc[artists_data_set['genres'] == '[]'].index, inplace=True)

genres = ['pop', 'rock', 'indie', 'metal', 'hip hop', 'rap', 'jazz', 'deep', 'folk', 'punk', 'classical', 'house',
          'classic', 'alternative', 'german', 'trap', 'swedish', 'modern', 'italian', 'japanese',
          'country', 'blues', 'russian', 'french', 'latin', 'soul', 'black', 'techno',
          'brazilian', 'music', 'finnish', 'funk', 'uk', 'piano', 'contemporary', 'australian', 'dutch', 'dance',
          'death', 'reggae', 'experimental', 'r&b', 'spanish', 'traditional', 'trance']

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(artists_data_set["genres"])


# Calculate aritst-artist similarity based on genre
def artist_genre_only(artist_data, n=50):
    similarity = cosine_similarity(doc_vectors[artist_data.name], doc_vectors)
    top_50_indices = np.argsort(similarity)[0, -n:]
    top_50_similar_artists = artists_data_set.iloc[top_50_indices][["name"]]
    top_50_similar_artists['g_similarity'] = np.take(similarity, top_50_indices)
    return top_50_similar_artists.values.tolist()


def worker(artist_data, n=50):
    print(f"Processing artist: {artist_data['name']}")
    aa_sim_genre = artist_genre_only(artist_data, n)
    return aa_sim_genre

