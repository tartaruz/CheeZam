from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

engine = create_engine("mysql+pymysql://" + '90567_schitzam' + ":" + 'PREBOBU53' + "@" + 'sql31.mcb.webhuset.no' + "/" + '90567_schitzam')

df = pd.read_csv('data/genre_songs.csv', engine='python', quotechar='"')
print(len(df.index))

dic = {}
ids = []
indexes_to_delete = []
for track_id in df['track.id']:
    if track_id not in ids:
        ids.append(track_id)
        indexes = list(df.index[df['track.id'] == track_id].values)
        if len(indexes) > 1:
            values = df.iloc[indexes, :]
            genres = {}
            for genre in values['playlist_genre']:
                genres[genre] = genres.get(genre, 0) + 1
            genreToKeep = sorted(list(genres.items()), key=lambda x: x[1], reverse=True)[0][0]
            index_to_keep = values.index[values['playlist_genre'] == genreToKeep].values[0]
            indexes.remove(index_to_keep)
            indexes_to_delete += indexes

df.drop(indexes_to_delete, inplace=True)

df_cases = df[0:len(df)//2]
df_test = df[len(df)//2:]

conn = engine.connect()

df_cases.to_sql('cases', conn, if_exists = 'replace')
df_test.to_sql('test_cases', conn, if_exists = 'replace')