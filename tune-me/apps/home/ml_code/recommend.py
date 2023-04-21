import pandas as pd
import time
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import rbf_kernel, cosine_similarity
import warnings
import numpy as np

# Ignoring warnings for better debugging
warnings.filterwarnings('ignore')

master_data_set = pd.read_csv(
    r"C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior Design\ml_code\data\data_set.csv")

master_data_set.drop("id", axis=1, inplace=True)

themes_data_set = pd.read_csv(r"C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior "
                              r"Design\ml_code\data\archive\themes.csv", encoding="ISO-8859-1")


def clean_query(query):
    query.pop("csrf_token")
    query.pop("search")
    for key, value in query.items():
        # convert from lists to appropriate format
        if value == ['']:
            query[key] = ''
        else:
            if key not in ["artists", "album_name", "song_title", "genres", "themes", "explicit"]:
                query[key] = float(query[key][0])
            else:
                query[key] = ' '.join(value)
    query["artists"] = query.pop("artist")
    query["track_genre"] = query.pop("genres")
    query["track_name"] = query.pop("song_title")
    query["acousticness"] = query.pop("acoustics")
    return query


def case(form_data):
    fields = list()
    for key, item in form_data.items():
        if item == '':
            continue
        else:
            fields.append(key)

    case_num = -1

    if 'track_name' in fields:
        case_num = 1

    elif len(fields) == 1:
        if 'artists' in fields:
            case_num = 2
        elif 'track_genre' in fields:
            case_num = 3
        elif 'year' in fields:
            case_num = 4
        elif 'themes' in fields:
            case_num = 5
        else:
            case_num = 6

    elif len(fields) == 2:
        if 'artists' in fields and 'year' in fields:
            case_num = 7
        elif 'artists' in fields and 'genre' in fields:
            case_num = 8
        elif 'artists' in fields and 'themes' in fields:
            case_num = 9
        elif 'track_genre' in fields and 'year' in fields:
            case_num = 10
        elif 'track_genre' in fields and 'themes' in fields:
            case_num = 11
        elif 'year' in fields and 'themes' in fields:
            case_num = 12
        elif 'artists' in fields or 'year' in fields or 'track_genre' in fields or 'themes' in fields:
            case_num = 13
        else:
            case_num = 14

    elif len(fields) == 3:
        if 'artists' in fields and 'year' in fields and 'track_genre' in fields:
            case_num = 15
        elif 'artists' in fields and 'year' in fields and 'themes' in fields:
            case_num = 16
        elif 'artists' in fields and 'track_genre' in fields and 'themes' in fields:
            case_num = 17
        elif 'year' in fields and 'track_genre' in fields and 'themes' in fields:
            case_num = 18
        elif 'artists' in fields and 'year' in fields and 'track_genre' in fields or 'themes' in fields:
            case_num = 19
        else:
            case_num = 20
    else:
        case_num = 21

    return case_num, fields


def find_songs(cleaned_query, n=5):
    _, fields = case(cleaned_query)
    recommendations = pd.DataFrame(columns=['artists', 'album_name', 'track_name', 'popularity', 'duration_ms',
                                            'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode',
                                            'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence',
                                            'tempo', 'time_signature', 'track_genre', 'year'])

    if 'track_name' in fields:  # query with a song name
        search_query = master_data_set[(master_data_set['track_name'] == cleaned_query['track_name'].upper()) & (
                    master_data_set['artists'] == cleaned_query['artists'])]
        num_fields = [field for field in fields if field not in ["track_name", "artists", 'track_genre', 'themes']]
        wordy_query = ''

        if not search_query.empty:
            search_query.drop("track_name", axis=1)
            track_wt = 1 / len(fields)
            numeric_wt = len(num_fields)/len(fields)
            wordy_wt = 1 - track_wt - numeric_wt
            if 'artists' in fields:
                wordy_query += search_query["artists"].str.cat(sep=' ')
            if 'track_genre' in fields:
                wordy_query += ' ' + search_query["track_genre"].str.cat(sep=' ')
            else:
                pass
        else:
            search_query = pd.DataFrame(0, columns=num_fields, index=[0])
            numeric_wt = len(num_fields)/len(fields)
            track_wt = 0
            wordy_wt = 1 - numeric_wt

        relevant_columns = master_data_set[num_fields]

        similarity_score_for_song = rbf_kernel(search_query[num_fields], relevant_columns, 0.1)

        search_query = pd.DataFrame(0, columns=num_fields, index=[0])
        for field in num_fields:
            search_query[field] = cleaned_query[field]

        similarity_score = rbf_kernel(search_query[num_fields], relevant_columns, 0.1)  # for numbers

        if any([field in ["artists", "track_genre", "themes"] for field in fields]):  # Account for wordy similiarity
            empty_list = [''] * master_data_set.shape[0]
            relevant_wordy_columns = pd.DataFrame({'wordy_corpus': empty_list})
            if 'artists' in fields:
                wordy_query += ' ' + cleaned_query["artists"]
                artist_column = master_data_set['artists'].apply((lambda x: ' '.join(x.split(';'))))
                relevant_wordy_columns['wordy_corpus'] = relevant_wordy_columns['wordy_corpus'] + ' ' + artist_column
            if 'track_genre' in fields:
                wordy_query += (' ' + cleaned_query["track_genre"] + ' ')
                genre_column = master_data_set['track_genre'].apply((lambda x: ' '.join(x.split(';'))))
                relevant_wordy_columns['wordy_corpus'] = relevant_wordy_columns['wordy_corpus'] + ' ' + genre_column
            else:  # themes
                pass  # TODO
            vectorizer = TfidfVectorizer()
            tfidf_vectors = vectorizer.fit_transform(relevant_wordy_columns['wordy_corpus'])
            query_vector = vectorizer.transform([wordy_query])
            cosine_similarities = cosine_similarity(tfidf_vectors, query_vector)
            if 'track_name' in fields:
                similarity_score = wordy_wt * cosine_similarities.T + numeric_wt * similarity_score + track_wt * similarity_score_for_song
            else:
                similarity_score = wordy_wt * cosine_similarities.T + numeric_wt * similarity_score
    else:  # query resembling one with a song name but does not have one
        num_fields = [field for field in fields if field not in ["artists", 'track_genre', 'themes']]
        search_query = {field: cleaned_query[field] for field in num_fields}
        search_query = pd.DataFrame(search_query, columns=num_fields, index=[0])
        relevant_columns = master_data_set[num_fields]
        similarity_score = rbf_kernel(search_query, relevant_columns, 0.1)

        if any([field in ["artists", "track_genre", "themes"] for field in fields]):  # Account for wordy similiarity
            wordy_query = ''
            empty_list = [''] * master_data_set.shape[0]
            relevant_wordy_columns = pd.DataFrame({'wordy_corpus': empty_list})
            if 'artists' in fields:
                wordy_query += cleaned_query["artists"]
                artist_column = master_data_set['artists'].apply((lambda x: ' '.join(x.split(';'))))
                relevant_wordy_columns['wordy_corpus'] = relevant_wordy_columns['wordy_corpus'] + ' ' + artist_column
            if 'track_genre' in fields:
                wordy_query += (cleaned_query["track_genre"] + ' ')
                genre_column = master_data_set['track_genre'].apply((lambda x: ' '.join(x.split(';'))))
                relevant_wordy_columns['wordy_corpus'] = relevant_wordy_columns['wordy_corpus'] + ' ' + genre_column
            else:  # themes
                pass  # TODO
            vectorizer = TfidfVectorizer()
            tfidf_vectors = vectorizer.fit_transform(relevant_wordy_columns['wordy_corpus'])
            query_vector = vectorizer.transform([wordy_query])
            cosine_similarities = cosine_similarity(tfidf_vectors, query_vector)
            numeric_wt = len(num_fields) / len(fields)
            wordy_wt = 1 - numeric_wt
            similarity_score = wordy_wt * cosine_similarities.T + numeric_wt * similarity_score
    similarity_score = np.argsort(similarity_score)[0, -1:-n:-1]

    recommendations = master_data_set.iloc[similarity_score]

    return recommendations


def single_param_query(cleaned_query, n=5, explicit=False):
    _, fields = case(cleaned_query)
    similarity_param, param_val = fields[0], cleaned_query[fields[0]]
    recommendations = master_data_set[master_data_set[similarity_param] == param_val].head(n)
    if similarity_param == 'artists':
        if len(recommendations) == 0:
            recommendations = None
        elif len(recommendations) < n:
            numeric_median = recommendations.median()
            numeric_median["artists"] = param_val
            numeric_median["track_genre"] = ' '.join(recommendations["track_genre"].astype(str))
            remaining_songs = find_songs(numeric_median, n - len(recommendations))
            recommendations = pd.concat(recommendations, remaining_songs) if remaining_songs != '' else recommendations
    elif similarity_param == 'track_genre':  # or similarity_param == 'themes':
        if len(recommendations) == 0:
            recommendations = None
        elif len(recommendations) < n:
            numeric_median = recommendations.median()
            numeric_median["artists"] = ' '.join(recommendations["artists"].astype(str))
            numeric_median["track_genre"] = param_val
            remaining_songs = find_songs(numeric_median, n - len(recommendations))
            recommendations = pd.concat(recommendations, remaining_songs) if remaining_songs != '' else recommendations
    else:
        if similarity_param == 'year':
            recommendations = master_data_set.iloc[(-master_data_set[similarity_param] + param_val).argsort()[:n]]
        else:
            recommendations = master_data_set.iloc[(master_data_set[similarity_param] - param_val).abs().argsort()[:n]]
    return recommendations


def two_param_queries(cleaned_query, n=5, explicit=False):
    _, fields = case(cleaned_query)
    similarity_params, param_vals = [fields[0], fields[1]], [cleaned_query[fields[0]], cleaned_query[fields[1]]]
    recommendations = None
    if 'artists' in similarity_params and (
            'year' in similarity_params or similarity_params[1] not in ['track_genre', 'themes']):
        # get all songs for artists, calculate median, get similar songs for year
        recommendations = master_data_set[master_data_set['artists'] == param_vals[0]]
        numeric_median = recommendations.median()
        numeric_median["artists"] = param_vals[0]
        numeric_median[similarity_params[1]] = param_vals[1]
        numeric_median["track_genre"] = ' '.join(recommendations["track_genre"].astype(str))
        recommendations = find_songs(numeric_median, n)
    elif 'artists' in similarity_params and 'track_genre' in similarity_params:
        # get all songs for artists, calculate median, get similar songs for genre
        recommendations = master_data_set[master_data_set['artists'] == param_vals[0]]
        numeric_median = recommendations.median()
        numeric_median["artists"] = param_vals[0]
        numeric_median["track_genre"] = param_vals[1]
        recommendations = find_songs(numeric_median, n)
    elif 'artists' in similarity_params and 'themes' in similarity_params:
        pass  # TODO
    elif 'track_genre' in similarity_params and ('year' in similarity_params or 'themes' != similarity_params[1]):
        recommendations = master_data_set[master_data_set['track_genre'] == param_vals[0]]
        if similarity_params[1] == 'year':
            recommendations = recommendations.iloc[(-recommendations['year'] + param_vals[1]).argsort()[:n]]
        else:
            recommendations = recommendations.iloc[
                (recommendations[similarity_params[1]] - param_vals[1]).abs().argsort()[:n]]
    elif 'track_genre' in similarity_params and 'themes' in similarity_params:
        pass  # TODO
    elif 'year' in similarity_params and 'themes' in similarity_params:
        pass  # TODO
    else:
        recommendations = find_songs(cleaned_query)
    return recommendations


def three_param_queries(cleaned_query, n=5):
    _, fields = case(cleaned_query)
    recommendations = None
    similarity_params, param_vals = fields, [cleaned_query[field] for field in fields]
    if 'artists' in fields and 'track_genre' in fields and 'themes' not in fields:
        # get all songs for artists, calculate median, get similar songs for year (other params)
        recommendations = master_data_set[master_data_set['artists'] == param_vals[0]]
        numeric_median = recommendations.median()
        numeric_median["artists"] = param_vals[0]
        numeric_median[similarity_params[1]] = param_vals[1]
        numeric_median[similarity_params[2]] = param_vals[2]
        recommendations = find_songs(numeric_median, n)
    elif 'artists' in fields and 'year' in fields and 'themes' in fields:
        pass  # TODO
    elif 'artists' in fields and 'track_genre' in fields and 'themes' in fields:
        pass  # TODO
    elif 'year' in fields and 'track_genre' in fields and 'themes' in fields:
        pass  # TODO
    else:
        recommendations = find_songs(cleaned_query)
    return recommendations


def recommend_songs(form_data):
    query = clean_query(form_data)
    query.pop("explicit")
    n = int(query.pop('num_tracks'))
    recommendations = None
    c, fields = case(query)
    if c in [1, 19, 20, 21]:  # Treat query as a song
        recommendations = find_songs(query, n)
    elif c in [2, 3, 4, 5, 6]:
        recommendations = single_param_query(query, n)
    elif c in [7, 8, 9, 10, 11, 12]:
        recommendations = two_param_queries(query, n)
    elif c in [14, 15, 16, 17, 18]:
        recommendations = three_param_queries(query, n)
    return recommendations


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(recommend_songs({'csrf_token': ['IjRlYTc0MmQ3MjAzODQxYzQxMWEyMmJjNmE0MTBhMjc0MzM2Y2Y3MGQi.ZEGBdg.wo0p_lmIC0A6H_0a_pjyU4MSuMk'],
                       'song_title': [''], 'artist': [''], 'year': [''], 'genres': ['rock'], 'popularity': ['13'], 'danceability': [''],
                       'energy': [''], 'loudness': [''], 'speechiness': ['44'], 'acoustics': [''], 'instrumentalness': [''],
                       'liveness': [''], 'valence': [''], 'tempo': [''], 'search': [''], 'num_tracks':['10'], 'explicit': ['n']}))