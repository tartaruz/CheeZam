from server.DB import DbConnector
from model.case import case

from help_modules.Spotify import Spotify
from help_modules.functions import caseFromQuery

from Retrieval import Retrieval
from Reuse import Reuse
from Revise import Revise
from Retain import Retain

class CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse(self.r1.cases)
        self.r3 = Revise(self.DB)
        self.r4 = Retain(self.DB)
        self.spotify = Spotify()
        self.query = None
        self.artist = None
        self.case = None
        self.artist_genres = []

    # Retrieval get an array with cases repesented as [case.track_id, similarity number(float 0.0 - 1.0)]
    def retrieve(self):
        self.r1.queryCase = self.case
        self.r1.knn(1)

    # Reuse 
    def reuse(self):
        similarCases = self.r1.similarCases
        self.r2.setQueryCase(self.case)
        self.r2.retrieval = self.r1
        self.r2.reuse(similarCases)
        
    def revision(self):
        self.r3.reuse = self.r2
        self.r3.case = self.case
        self.r3.revise()
        self.r2.predictionGenre = self.case.playlist_genre
        self.r2.predictionSubGenre =self.case.playlist_subgenre
        print()

    def retain(self):
        print(f'Info about "{self.case.track_name}\nGenre: {self.case.playlist_genre}\nSubgenre: {self.case.playlist_subgenre} \n')
        self.r4.setCase(self.case)
        self.r4.retain()

    def setQuery(self):
        self.query = input('Please input a song title to predict genre: ').lower()
        self.artist = input('Please enter artist of the song: ').lower()
        print()
        self.DB.open_connection()
        self.case = case(caseFromQuery(self))



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
    cbr.retain()


if __name__ == '__main__':
    main()
