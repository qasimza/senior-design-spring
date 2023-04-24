import lyricsgenius as lg
import csv
import multiprocessing as mp

genius = lg.Genius('wCZurTUKVZgBeZeW-rH3G5IORBQJdiwKRwGY6vtZ32q91WLINjBzrOV9fv8ppD3Q',
                   skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

csvfile = open(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior Design\ml_code\data\archive\themes.csv',
               newline='', encoding='ISO-8859-1')

themes_data = csv.reader(csvfile)

out_file = open(r"C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior "
                   r"Design\ml_code\data\archive\themes-lyrics.csv", 'a', encoding='utf-8')

writer = csv.writer(out_file)

def find_lyrics(row):
    try:
        song_name = row[0]
        artist_name = row[1]
        lyrics = genius.search_song(title=song_name, artist=artist_name).lyrics
        lyrics = lyrics.replace("\n", " ")
    except:
        lyrics = None
    return lyrics


def worker(row):
    lyrics = find_lyrics(row)
    if lyrics is not None:
        row.append(lyrics)
        try:
            writer.writerow(row)
        except:
            print(f"Could not write: {row}")


if __name__ == '__main__':
    pool = mp.Pool(8)
    pool.map(worker, themes_data)