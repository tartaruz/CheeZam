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

def retiveCases():
    DB.cursor.execute("SELECT * FROM cases")
    result = DB.cursor.fetchall()
    return [case(data) for data in result]

cases = retiveCases()
data = cases[10]
NN = knn(cases, data, 4)
print(data.track_name+" - "+data.playlist_genre)
print([case.track_name+" - "+case.track_artist+" - "+case.playlist_genre for case in NN])