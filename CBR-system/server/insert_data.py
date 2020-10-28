from sqlalchemy import create_engine
import pymysql
import pandas as pd

engine = create_engine("mysql+pymysql://" + '90567_schitzam' + ":" + 'PASSWORD' + "@" + 'sql31.mcb.webhuset.no' + "/" + '90567_schitzam')
conn = engine.connect()

df = pd.read_csv('data/genre_songs.csv', engine='python', quotechar='"')

df.to_sql('cases', conn, if_exists = 'replace')