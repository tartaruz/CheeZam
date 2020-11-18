class Revise:

    def __init__(self, DB, user):
        # self.genres = ['Pop', 'Rap', 'Rock', 'Latin', 'R&B', 'EDM']
        # self.subgenres = ['dance pop', 'post-teen pop', 'electropop', 'indie poptimism', 'hip hop', 'southern hip hop', 'gangster rap', 'trap', 'album rock', 'classic rock', 'permanent wave', 'hard rock', 'tropical', 'latin pop', 'reggaeton', 'latin hip hop', 'urban contemporary', 'hip pop', 'new jack swing', 'neo soul', 'electro house', 'big room', 'pop edm', 'progressive electro house']
        self.reuse = None
        self.case = None
        self.genre = None
        self.subgenre = None
        self.user = user
        self.DB = DB
        self.DB.open_connection()
        self.DB.cursor.execute('SELECT DISTINCT playlist_genre FROM cases;')
        self.genres = [genre[0].capitalize()
                       for genre in self.DB.cursor.fetchall() if not genre[0] == None]
        self.DB.cursor.execute('SELECT DISTINCT playlist_subgenre FROM cases;')
        self.subgenres = [subgenre[0].capitalize()
                          for subgenre in self.DB.cursor.fetchall() if not subgenre[0] == None]
        self.DB.close_connection()

    def revise(self):
        self.user.revision = self
        # CBR, new_case, artist_genres
        self.genres = list(set([genre.capitalize() for genre in self.genres]))

        answer = self.user.consol_print("first_predict")
        print()

        # If correct prediciton
        if answer.lower() == 'y':
            self.genre = self.reuse.predictionGenre[0]
        # If incorrect, predict new genre
        else:
            ans = self.user.consol_print("choose_genre")

        satisfied = self.user.consol_print(
            "predict_subgenre", (answer.lower() == 'y'))

        if satisfied.lower() == 'y':
            self.subgenre = self.reuse.predictionSubGenre
        else:
            print(self.subgenres)
            ans = self.user.consol_print("choose_subgenre", subgenres=self.subgenres)
            self.subgenre = ans

        print()
        print('Thank you for your answers!')

        # Update the case to predicitons or decitions
        self.case.playlist_genre = self.genre
        self.case.playlist_subgenre = self.subgenre


   