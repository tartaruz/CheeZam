class Revise:
    """
    A class to represent the third R in the 4R cycle - Revise. 
    The class will revise the proposed solution based on user input.
    ...

    Attributes
    ----------
    reuse : Reuse
        Reuse object
    case : Case
        Case object for the song the user has inputed
    genre : String
        The predicted genre or revised genre, based on user input
    subGenre : String
        The predicted sub-genre or revised genre, based on user input
    user : User
        User object to handle input/output
    DB : DB
         Database object
    genres : List
        List of all genres in the case base
    subGenres : List
        List of all sub-genres in the case base
    Methods
    -------
    revise():
        Will ask the user questions about the predicted genre and subgenre, and update theese if the user are not satisfied
    """
    def __init__(self, DB, user):
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
        """Will ask the user questions about the predicted genre and subgenre, and update theese if the user are not satisfied"""
        self.user.revision = self
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


   