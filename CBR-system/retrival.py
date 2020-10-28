from server.DB import DbConnector
from case import case
import math

DB = DbConnector()

def euclidian_distance(v1, v2):
    summation =  0
    for i in range(len(v1)):
        summation += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(summation)

def knn(cases, queryCase, K):
    # Initializing dict of distances and variable with size of training set
    distances = {}
    casesValues = [c.returnNumericValue() for c in cases]
    # Calculating the Euclidean distance between the new
    # sample and the values of the training sample
    for i in range(len(casesValues)):
        d = euclidian_distance(casesValues[i], queryCase.returnNumericValue())
        distances[i] = d
    
    # Selecting the K nearest neighbors
    k_neighbors = sorted(distances, key=distances.get)[:]
    
    return [cases[index] for index in k_neighbors[:K]]


def voteKNN(cases, queryCase, K_votes):
    casesSimilar = knn(cases, queryCase, K_votes)
    genres = [case.playlist_genre for case in casesSimilar]
    sort = [[x,genres.count(x)] for x in set(genres)]
    sort.sort(key=lambda count: count[1], reverse=True)
    if sort[0][1]>1:
        return sort[0][0]
    else:
        return None

def retiveCases():
    DB.cursor.execute("SELECT * FROM cases")
    result = DB.cursor.fetchall()
    return [case(data) for data in result]


cases = retiveCases()
data = cases[10]

votes = voteKNN(cases, data, 10)
print(votes)