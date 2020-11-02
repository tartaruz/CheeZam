class Reuse:
    def __init__(self, cases,epsilon=10):
        self.queryCase = None
        self.retrieval = None
        self.predictionCase = None
        self.predictionGenre = None
        self.epsilon = epsilon
        self.cases = cases
        
    
    def reuse(self, similarCases):
        epsilonAcceptedCases = [case for case in similarCases if case[1]>self.epsilon]
        # Pigeonhole principle since we got 6 main genres
        if len(epsilonAcceptedCases)<=0:
            genre = self.voteKNN(self.queryCase, 7)
            self.predictionGenre = genre
        else:
            self.predictionCase = list(filter(lambda x: x.track_id == epsilonAcceptedCases[0][0], self.cases))[0]
            self.predictionGenre = self.predictionCase.playlist_genre

    
    def setQueryCase(self, q):
        self.queryCase = q

    def retrive(self,retrieval,queryCase, K):
        self.retrieval = retrieval.knn(queryCase, K)

    
    def voteKNN(self, queryCase, K_votes):
        casesSimilar = self.retrieval.knn(queryCase, K_votes)
        genres = [case[0].playlist_genre for case in casesSimilar]
        sort = [[x,genres.count(x)] for x in set(genres)]
        sort.sort(key=lambda count: count[1], reverse=True)
        if sort[0][1]>1:
            return sort[0][0]
        else:
            return None

    