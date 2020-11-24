import sys
import random

from server.DB import DbConnector
from model.case import case

from help_modules.Spotify import Spotify
from help_modules.functions import caseFromQuery
from help_modules.tester import Tester

from Retrieval import Retrieval
from Reuse import Reuse
from Revise import Revise
from Retain import Retain

from user import User
class CBR:
    """
    A class to represent a CBR system.

    ...

    Attributes
    ----------
    DB : DB
        Database object
    user : User
        User object to handle input/output from/to the user
    r1 : Retrieval
        The first R in the 4R cycle - retrieval
    r2 : Reuse
        The second R in the 4R cycle - reuse
    r3 : Revise
        The third R in the 4R cycle - Revise
    r4 : Retain
        The fourth R in the 4R cycle - Retain
    spotify : Spotify
        Spotify object to handle requests to the Spotify API
    query : str
        The user's song input
    artist : str
        The user's artist input
    case : Case
        Case object for the song the user has inputed
    artist_genres : list
        The genres the artist the user has inputed most frequently makes song in
    predictionCase : Case
        The predicted and retrieved best case

    Methods
    -------
    retrieve():
        Retrieves all cases and does 1NN on them and the new case
    reuse():
        Checks whether an old solution can be reused or if KNN are needed
    revise():
        Checks whether the solution is a valid solution, by asking the user if it's ok
    retain():
        Stores the new soluton in the case base
    setQuery(tester=None):
        Asks the user for a song input and creates a new case based on the input
    """
    def __init__(self, testing=False):
        self.DB = DbConnector()
        self.user = User()
        self.DB.open_connection()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse(self.r1.cases)
        self.r3 = Revise(self.DB, self.user)
        self.r4 = Retain(self.DB)
        self.spotify = Spotify()
        self.query = None
        self.artist = None
        self.case = None
        self.artist_genres = []
        self.predictionCase = None
        
        self.testing = testing
        self.testCases = None

    # Retrieval get an array with cases repesented as [case.track_id, similarity number(float 0.0 - 1.0)]
    def retrieve(self):
        """Retrieves all cases and does 1NN on them and the new case"""
        self.DB.close_connection()
        self.r1.queryCase = self.case
        self.r1.knn(1)

    # Reuse 
    def reuse(self):
        """Checks whether an old solution can be reused or if KNN are needed"""
        similarCases = self.r1.similarCases
        self.r2.setQueryCase(self.case)
        self.r2.retrieval = self.r1
        self.r2.reuse(similarCases)
        self.predictionCase = self.r2.predictionCase
        
    def revision(self):
        """Checks whether the solution is a valid solution, by asking the user if it's ok"""
        self.r3.reuse = self.r2
        self.r3.case = self.case
        self.r3.revise()
        self.r2.predictionGenre = self.case.playlist_genre
        self.r2.predictionSubGenre =self.case.playlist_subgenre
        print()

    def retain(self):
        """Stores the new soluton in the case base"""
        self.r4.setCase(self.case, self.predictionCase)      
        self.DB.open_connection()
        self.r4.retain()
        self.DB.close_connection()

    def setQuery(self, tester=None):
        """Asks the user for a song input and creates a new case based on the input"""
        if self.testing:
            self.user = tester
            self.r3.user = self.user
            self.query, self.artist = self.user.search()
            self.case = tester.case
        else:
            self.user = User()
            self.r3.user = self.user
            self.query, self.artist = self.user.search()
            self.case = case(caseFromQuery(self))
        self.DB.open_connection()


def main():
    cbr = CBR()
    cbr.setQuery()

    # kNN with K=1  ----> 1-NN
    cbr.retrieve()
    
    # Use the closes neighbor, or have an votation for findng genre data
    cbr.reuse()
    
    #much fun
    cbr.revision()

    #saves if dont exist
    if not cbr.testing:
        cbr.retain()


if __name__ == '__main__':
    main()
