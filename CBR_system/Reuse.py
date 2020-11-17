import math
class Reuse:
    def __init__(self, cases,epsilon=5):
        self.queryCase = None
        self.retrieval = None
        self.predictionCase = None
        self.predictionGenres = None
        self.predictionSubGenres = None
        self.genres = []
        self.subgenres = []
        self.epsilon = epsilon
        self.cases = cases
        self.subgenres_cases = None
        self.genres_cases = None
        
    
    def reuse(self, similarCases):
        epsilonAcceptedCases = [case for case in similarCases if case[1]<=self.epsilon]
        # Pigeonhole principle since we got 6 main genres
        
        if len(epsilonAcceptedCases)<=0:
            print("VNN")
            self.voteKNN(self.queryCase, 30)
            self.predictionGenre = self.genres[0]
            self.predictionSubGenre = self.subgenres[0]
            print(self.genres)

        else:
            print("no VNN")
            print()
            predictionCase = list(filter(lambda x: x.track_id == epsilonAcceptedCases[0][0], self.cases))[0]
            self.predictionGenre = [predictionCase.playlist_genre]
            self.predictionSubGenre = [predictionCase.playlist_subgenre]
            self.genres = [[predictionCase.playlist_genre,1]]
            self.subgenres = [[predictionCase.playlist_subgenre,1]]


    
    def setQueryCase(self, q):
        self.queryCase = q

    def retrive(self,retrieval,queryCase, K):
        self.retrieval = retrieval.knn(queryCase, K)

    
    def voteKNN(self, queryCase, K_votes):
        # print(queryCase, K_votes)
        self.retrieval.queryCase = queryCase
        self.retrieval.knn(K_votes)
        # print(self.retrieval.retrievedCases)
        genres = [case.playlist_genre for case in self.retrieval.retrievedCases]
        sub_genres = [case.playlist_subgenre for case in self.retrieval.retrievedCases]
        
        newVotationCases = [[case[0].playlist_genre, 1/(case[1])] for case in self.retrieval.neighbors]
        counter = {}

        for vote in newVotationCases:
            # print(vote[0], (1 / (self.retrieval.genreCount[vote[0]]/ len(self.cases))))
            if vote[0] in counter:
                # counter[vote[0]] += (1 / (self.retrieval.genreCount[vote[0]]/ len(self.cases)))
                # counter[vote[0]] += vote[1]
                counter[vote[0]] += ((self.retrieval.genreCount[vote[0]]/ len(self.cases)))*vote[1]
            else:
                # counter[vote[0]] = (1 / (self.retrieval.genreCount[vote[0]] / len(self.cases)))
                # counter[vote[0]] = vote[1]
                counter[vote[0]] = ((self.retrieval.genreCount[vote[0]]/ len(self.cases)))*vote[1]
        print([ [k,v] for k,v in counter.items()])
        
        genres_sort = [ [k,v] for k,v in counter.items()]
        genres_sort.sort(key=lambda count: count[1], reverse=True)
        
        sub_genres_sort = [[x,sub_genres.count(x)] for x in set(sub_genres)]
        sub_genres_sort.sort(key=lambda count: count[1], reverse=True)
        
        self.genres = genres_sort
        self.subgenres = sub_genres_sort

        

    def genreSort(self, genres):
        genres_sort = [[x,genres.count(x)] for x in set(genres)]
        genres_sort.sort(key=lambda count: count[1], reverse=True)
        return genres_sort