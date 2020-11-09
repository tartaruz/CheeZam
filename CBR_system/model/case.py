class case:
    def __init__(self, fetchData):
        self.sqlData = fetchData
        self.index = fetchData[0]
        self.track_id = fetchData[1] 
        self.track_name = fetchData[2]
        self.track_artist = fetchData[3]
        self.track_popularity = fetchData[4]
        self.track_album_id  = fetchData[5]
        self.track_album_name  = fetchData[6]
        self.track_album_release_date = fetchData[7]
        self.playlist_name  = fetchData[8]
        self.playlist_id =  fetchData[9]
        self.playlist_genre = fetchData[10]
        self.playlist_subgenre  = fetchData[11]
        self.danceability =  fetchData[12]
        self.energy = fetchData[13]
        self.key_value  = fetchData[14]
        self.loudness  = fetchData[15]
        self.mode  = fetchData[16]
        self.speechiness  = fetchData[17]
        self.acousticness = fetchData[18]
        self.instrumentalness = fetchData[19]
        self.liveness =  fetchData[20]
        self.valence  = fetchData[21]
        self.tempo  = fetchData[22]
        self.duration_ms = fetchData[23]

    # Returnerer verdier for sammelingning
    def returnNumericValue(self):
        return list(map(lambda x: round(x, 4), [
                self.danceability,
                self.energy,
                self.key_value,
                self.loudness,
                self.mode,
                self.speechiness,
                self.acousticness,
                self.instrumentalness,
                self.liveness,
                self.valence,
                self.tempo,
                self.duration_ms
                ]))

    def toDict(self):
        return {
            'track_id': self.track_id,
            'track_name': self.track_name,
            'track_artist': self.track_artist,
            'track_popularity': self.track_popularity,
            'track_album_id': self.track_album_id,
            'track_album_name':self.track_album_name,
            'track_album_release_date': self.track_album_release_date,
            'playlist_name': self.playlist_name,
            'playlist_id': self.playlist_id,
            'playlist_genre': self.playlist_genre,
            'playlist_subgenre': self.playlist_subgenre,
            'danceability': self.danceability,
            'energy': self.energy,
            'key': self.key_value,
            'loudness': self.loudness,
            'mode': self.mode,
            'speechiness': self.speechiness,
            'acousticness': self.acousticness,
            'instrumentalness': self.instrumentalness,
            'liveness': self.liveness,
            'valence': self.valence,
            'tempo': self.tempo,
            'duration_ms': self.duration_ms
            }

    def setValues(self, genre, subgenre):
        self.playlist_genre = genre
        self.playlist_subgenre = subgenre


    def __str__(self):
        string = "Genre: \t"+  str(self.playlist_genre).title() +" ( "+ str(self.playlist_subgenre).title()+" ) \n"
        string += "Name: \t"+str(self.track_name)+" "+str(self.track_artist)+"\n"
        string += "Artist\t: \t"+ str(self)+"\n"
        string += "ID: \t"+ str(self.track_id)+"\n"
        return string