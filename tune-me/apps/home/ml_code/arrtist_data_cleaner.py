import pandas as pd

artists_data_set = pd.read_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                              r'Design\ml_code\data\archive\artists_cleaned.csv')

# unique genres
list_of_genres = {'pop', 'rock', 'indie', 'metal', 'hip-hop', 'rap', 'jazz', 'deep', 'folk', 'punk', 'classical',
                  'house', 'classic', 'alternative', 'german', 'trap', 'swedish', 'modern', 'italian', 'japanese',
                  'country', 'blues', 'russian', 'french', 'latin', 'soul', 'black', 'techno', 'brazilian', 'music',
                  'finnish', 'funk', 'uk', 'piano', 'contemporary', 'australian', 'dutch', 'dance', 'death', 'reggae',
                  'experimental', 'r&b', 'spanish', 'traditional', 'trance'}

for i in range(0, artists_data_set.shape[0]):
    genre = artists_data_set.iloc[i]["genres"]
    arr = genre.replace('[', '').replace(']', '').replace('"', '').replace('\'', '').replace(', ', ',').replace(
        'hip hop', 'hip-hop').split(',')
    arr = ' '.join(arr).split(' ')
    common = list_of_genres.intersection(set(arr))
    artists_data_set.at[i, 'genres'] = list(common)
    print(i)

genrestr = ' '.join(list_of_genres)

artists_data_set.to_csv(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior '
                        r'Design\ml_code\data\archive\artists_cleaned_genres.csv')

exit()

# Following code was used to find top relevant genres
import heapq
from collections import Counter


def most_frequent_word(test_list):
    all_words = [sub.split() for sub in test_list]
    word_counts = Counter(word for sublist in all_words for word in sublist)
    return heapq.nlargest(50, word_counts, key=word_counts.get)


test_list = genrestr.split(' ')

most_frequent_genre = most_frequent_word(test_list)
print("Word with most frequency: ", most_frequent_genre, len(most_frequent_genre))

exit()

