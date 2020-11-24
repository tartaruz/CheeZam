import math
class Reuse:
    """
    A class to represent the second R in the 4R cycle - Reuse. 
    Will check whether the predicted case from 1NN are "close engough" (distance <= 5).
    If it is not, KNN with K = 11 will be preformed
    ...

    Attributes
    ----------
    queryCase : Case
        Case from users input
    retrieval : Retrieval
        Retrieval object
    predictionCase : Case
        The predicted case
    predictionGenre : String
        The predicted genre
    predictionSubGenre : String
        The predicted sub-genre
    genres : List
        List that holds how many there are of each of the retrieved genres (from KNN with k = 11). Has the form [[genre_1, count_1], ..., [genre_k, count_k]]
    subgenres : List
        List that holds how many there are of each of the retrieved sub-genres (from KNN with k = 11). Has the form [[sub-genre_1, count_1], ..., [sub-genre_k, count_k]]
    epsilon : Integer
        Threshold for how close a case has to be to be accepted as the "winning" prediction case.
    cases : List
        List of all cases in the case base.
    subgenres_cases : List
        ?
    self.genres_cases : List
        ?
    
    Methods
    -------
    reuse(silimarCases):
        Checks whether the retrieved case from 1NN are close enough and sets the predicted genre and subgenre if it is.
        If it's too far away, it will call voteKNN().
    setQueryCase(q):
        Sets the case from the user's input
    retrieve(retrieval, case, K):
        Perform KNN with k = K on case and the case base from retrieval.
    voteKNN(queryCase, K_votes):
        Do KNN with k = K_votes and queryCase. After the retrieval of the K_votes nearest neighbours, multiply each of the
        distances with a weight and each of the genre counts in the retrieved cases with a weight, to "flatten" the results.
        Sets the variables self.genres and self.subgenres in ordered fashion, based on the distance from queryCase.
    """
    def __init__(self, cases,epsilon=5):
        self.queryCase = None
        self.retrieval = None
        self.predictionCase = None
        self.predictionGenre = None
        self.predictionSubGenre = None
        self.genres = []
        self.subgenres = []
        self.epsilon = epsilon
        self.cases = cases
        # self.subgenres_cases = None
        # self.genres_cases = None
        
    
    def reuse(self, similarCases):
        """
        Checks whether the retrieved case from 1NN are close enough and sets the predicted genre and subgenre if it is.
        If it's too far away, it will call voteKNN().
        """
        epsilonAcceptedCases = [case for case in similarCases if case[1]<=self.epsilon]
        # KNN-Classification, Number 11 sat at line 23
        if len(epsilonAcceptedCases)<=0:
            self.voteKNN(self.queryCase, 11)
            self.predictionGenre = self.genres[0]
            self.predictionSubGenre = self.subgenres[0]

        else:
            print()
            predictionCase = list(filter(lambda x: x.track_id == epsilonAcceptedCases[0][0], self.cases))[0]
            self.predictionCase = predictionCase
            self.predictionGenre = [predictionCase.playlist_genre]
            self.predictionSubGenre = [predictionCase.playlist_subgenre]
            self.genres = [[predictionCase.playlist_genre,1]]
            self.subgenres = [[predictionCase.playlist_subgenre,1]]

    
    def setQueryCase(self, q):
        """Sets the case from the user's input"""
        self.queryCase = q

    def retrive(self,retrieval,queryCase, K):
        """Perform KNN with k = K on case and the case base from retrieval."""
        self.retrieval = retrieval.knn(queryCase, K)

    
    def voteKNN(self, queryCase, K_votes):
        """
        Do KNN with k = K_votes and queryCase. After the retrieval of the K_votes nearest neighbours, multiply each of the
        distances with a weight and each of the genre counts in the retrieved cases with a weight, to "flatten" the results.
        Sets the variables self.genres and self.subgenres in ordered fashion, based on the distance from queryCase.
        """
        self.retrieval.queryCase = queryCase
        self.retrieval.knn(K_votes)
        sub_genres = [case.playlist_subgenre for case in self.retrieval.retrievedCases]
        
        newVotationCases = [[case[0].playlist_genre, 1/(case[1])] for case in self.retrieval.neighbors]
        counter = {}

        for vote in newVotationCases:
            if vote[0] in counter:
                counter[vote[0]] += ((self.retrieval.genreCount[vote[0]]/ len(self.cases)))*vote[1]
            else:
                counter[vote[0]] = ((self.retrieval.genreCount[vote[0]]/ len(self.cases)))*vote[1]
        genres_sort = [ [k,v] for k,v in counter.items()]
        genres_sort.sort(key=lambda count: count[1], reverse=True)
        
        sub_genres_sort = [[x,sub_genres.count(x)] for x in set(sub_genres)]
        sub_genres_sort.sort(key=lambda count: count[1], reverse=True)
        
        self.genres = genres_sort
        self.subgenres = sub_genres_sort

        
