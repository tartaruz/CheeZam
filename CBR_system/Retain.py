class Retain:

    def __init__(self, DB):
        self.case = None
        self.DB = DB
    
    def setCase(self,case):
        self.case = case

    def check_exist(self):
        self.DB.cursor.execute("SELECT `track.id` FROM cases WHERE `track.id` = \""+self.case.track_id+"\";")
        fetchedCase = self.DB.cursor.fetchall()
        print(fetchedCase)
        return (len(fetchedCase)>0)

    def retain(self):
        self.DB.open_connection()
        if (self.case != None and not self.check_exist()):
            query = self.sqlQuery()
            print("[Case inserted to DB]")

        else:
            print("[Case updated inserted to DB]")
            query = f"""
            UPDATE cases 
            SET
                `playlist_genre` = "{self.case.playlist_genre}",
                `playlist_subgenre` = "{self.case.playlist_subgenre.lower()}"
            WHERE
                `track.id` = "{self.case.track_id}"
            """        
        self.DB.cursor.execute(query)
        self.DB.db_connection.commit()
        print(self.case)
        self.DB.close_connection()

    # LOOK WHAT SANDER MADE ME DOOOO
    def sqlQuery(self):
        caseDict = self.case2query()
        col = ", ".join(["`"+str(col)+"`" for col in caseDict.keys()])
        values = ", ".join(["\""+str(value)+"\"" for value in caseDict.values()])
        q = "INSERT INTO cases ("+col+")"
        q += " VALUES ("+values+");"
        return q
        
    def case2query(self):
        case = self.case
        return {
            'track.id': case.track_id,
            'track.name': case.track_name,
            'track.artist': case.track_artist,
            'track.popularity': case.track_popularity,
            'track.album.id': case.track_album_id,
            'track.album.name':case.track_album_name,
            'track.album.release_date': case.track_album_release_date,
            'playlist_name': case.playlist_name,
            'playlist_id': case.playlist_id,
            'playlist_genre': case.playlist_genre,
            'playlist_subgenre': case.playlist_subgenre,
            'danceability': case.danceability,
            'energy': case.energy,
            'key': case.key_value,
            'loudness': case.loudness,
            'mode': case.mode,
            'speechiness': case.speechiness,
            'acousticness': case.acousticness,
            'instrumentalness': case.instrumentalness,
            'liveness': case.liveness,
            'valence': case.valence,
            'tempo': case.tempo,
            'duration_ms': case.duration_ms
            }