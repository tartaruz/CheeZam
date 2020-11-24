class Retain:
    """
    A class to represent the fourth R in the 4R cycle - Retain. Stores a new case in the case base.
    ...

    Attributes
    ----------
    case : Case
        The case to be stored in the case base
    DB : DB
        Database object
    
    Methods
    -------
    setCase(case):
        Sets case to be the class' case
    check_exists():
        Checks whether the case to be stored already exists in the case base
    retain():
        Retains the new case in the case base
    sqlQuery():
        Formats a case into sql statement
    case2Query():
        Formats a case to the format in the database
    """
    def __init__(self, DB):
        self.case = None
        self.predicted = None
        self.DB = DB
    
    def setCase(self,case, predicted):
        self.case = case
        self.predicted = predicted

    def check_exist(self):
        """Checks whether the case exists in the case base"""
        self.DB.cursor.execute("SELECT `track.id` FROM cases WHERE `track.id` = \""+self.case.track_id+"\";")
        fetchedCase = self.DB.cursor.fetchall()
        return (len(fetchedCase)>0)

    def retain(self):
        """
        Stores the case in the case base.

        If the case already exists, it will update the genre and subgenre to the new preticted genre.
        If it does not exist, it will create a new case in the case base.
        """
        try:
            self.DB.open_connection()
            if (self.case != None and not self.check_exist()):
                query = self.sqlQuery()
                # print("[Case inserted to DB]")

            else:
                # print("[Case updated inserted to DB]")
                query = f"""
                UPDATE cases 
                SET
                    `playlist_genre` = "{self.case.playlist_genre}",
                    `playlist_subgenre` = "{self.case.playlist_subgenre.lower()}"
                WHERE
                    `track.id` = "{self.predicted.track_id}"
                """    
            self.DB.cursor.execute(query)
            self.DB.db_connection.commit()
            self.DB.close_connection()
        except TypeError as e:
            print(e)
            pass
        
    def sqlQuery(self):
        """Formats the case into a SQL query"""
        caseDict = self.case2query()
        col = ", ".join(["`"+str(col)+"`" for col in caseDict.keys()])
        values = ", ".join(["\""+str(value)+"\"" for value in caseDict.values()])
        q = "INSERT INTO cases ("+col+")"
        q += " VALUES ("+values+");"
        return q
        
    def case2query(self):
        """Formats the case to the format used in the database"""
        case = self.case
        
        return {
            'track.id': case.track_id,
            'track.name': case.track_name.replace('"',"''"),
            'track.artist': case.track_artist.replace('"',"''"),
            'track.popularity': case.track_popularity,
            'track.album.id': case.track_album_id,
            'track.album.name':case.track_album_name.replace('"',"''"),
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