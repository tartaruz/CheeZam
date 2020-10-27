import pandas as pd
from DB import DbConnector as db

DB = db()

data = pd.read_csv("data/genre_songs.csv",  engine='python', quotechar='"')

print(data["track.id"][0])