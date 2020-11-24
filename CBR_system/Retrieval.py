from model.case import case
import math
import random

class Retrieval:
    """
    A class to represent the first R in the 4R cycle - Retrieval. 
    Retrieves all cases from the DB and does 1NN on them and the new case (from the user). 
    It uses euclidean distance as distance calculation.
    ...

    Attributes
    ----------
    DB : DB
        Database object
    cases : List
        All cases in the case base
    genreCount : Int
        Count of different genres in the case base. Used for weighting.
    queryCase : Case
        The newly created case from the user's input
    similarCases : List
        List of the k nearest cases after 1NN or KNN are performed on the form [[track.id_1, index_1], ..., [track.id_k, index_k]]
    retrievedCases : List
         List of the k nearest cases after 1NN or KNN are perfomed on the form [case_1, ..., case_k]
    neighbours : List
        List of the k nearest cases after 1NN or KNN are perfomed on the form [[case_1, distance_1], ..., [case_k, distance_k]]
    Methods
    -------
    euclidean_distance(v1, v2):
        Calculates euclidean distance between vector v1 and vector v2
    knn(K):
        Performes KNN with k = K
    retrieve_weights():
        Counts how many genres there are of each in the case base
    retrieveCases():
        Retrieves cases from the case base
    """
    def __init__(self, DB):
        self.DB = DB
        self.cases = self.retiveCases()
        self.genreCount = self.retrive_weigths()
        self.queryCase = None
        self.similarCases = None
        self.retrievedCases = None
        self.neighbors = []

    def euclidian_distance(self,v1, v2):
        """Calculates euclidean distance between vector v1 and vector v2"""
        summation =  0
        for i in range(len(v1)):
            summation += math.pow(v1[i] - v2[i], 2)
        return math.sqrt(summation)

    def knn(self, K):
        """
        Performes KNN with k = K.
        Sets the variables similarCases, retrievedCases and neighbours.
        """
        distances = {}
        casesValues = [c.returnNumericValue() for c in self.cases]
        
        for i in range(len(casesValues)):
            d = self.euclidian_distance(casesValues[i], self.queryCase.returnNumericValue())
            distances[i] = d
                 
        # Selecting the K nearest neighbors
        k_neighbors = [[key, value] for key, value in sorted(distances.items(), key=lambda case: case[1])][:K]   # [index, sdistance]
        self.similarCases = [[self.cases[index[0]].track_id,index[1]] for index in k_neighbors] 
        self.retrievedCases = [list(filter(lambda x: x.track_id == track_id, self.cases))[0] for track_id in map(lambda x: x[0], self.similarCases)] #[ track.id, distance]
        self.neighbors = [[self.cases[key], value] for key, value in sorted(distances.items(), key=lambda case: case[1])][:K]
        
    def retrive_weigths(self):
        """Counts how many genres there are of each in the case base"""
        genreCounter = {}
        for case in self.cases:
            if case.playlist_genre in genreCounter:
                genreCounter[case.playlist_genre] +=1
            else:
                genreCounter[case.playlist_genre] = 1
        return genreCounter
    
    def retiveCases(self):
        """Retrieves cases from the case base"""
        self.DB.cursor.execute("SELECT * FROM cases")
        result = self.DB.cursor.fetchall()
        return [case(data) for data in result]


