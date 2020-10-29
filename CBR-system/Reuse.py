class Reuse:
    def __init__(self, epsilon=10):
        self.queryCase = None
        self.retrieval = None
        self.epsilon = epsilon
    
    def reuse(self):

    
    def setQueryCase(self, q):
        self.queryCase = q

    def retrive(self,retrieval,queryCase, K):
        self.retrieval = retrieval.knn(queryCase, K)

    
    def voteKNN(self, queryCase, K_votes):
        casesSimilar = selsf.retrieval.knn(queryCase, K_votes)
        genres = [case[0].playlist_genre for case in casesSimilar]
        sort = [[x,genres.count(x)] for x in set(genres)]
        sort.sort(key=lambda count: count[1], reverse=True)
        if sort[0][1]>1:
            return sort[0][0]
        else:
            return None

    