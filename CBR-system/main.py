from server.DB import DbConnector
from Retrieval import Retrieval
from Reuse import Reuse
from model.case import case


query = [12029,"7tFiyTwD0nx5a1eklYtX2J","Bohemian Rhapsody - 2011 Mix","Queen",
            75,"6X9k3hSsvQck2OfKYdBbXr","A Night At The Opera (Deluxe Remastered Version)",
            1975-11-21,"Classic Rock Drive","37i9dQZF1DXdOEFt9ZX0dh",
            "rock","classic rock",0.392,0.402,0,-9.961,0,0.0536,0.28800000000000003,
            0,0.243,0.228,143.88299999999998,354320]

class CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse(self.r1.cases)

    def retive(self, query, k):
        # [2,3,2,3,2,3,23]
        queryCase =  case(query)
        self.r1.queryCase = queryCase
        self.r1.knn(k)

    def reuse(self):
        similarCases = self.r1.similarCases
        self.r2.retrieval = self.r1
        self.r2.reuse(similarCases)





CBR = CBR()
CBR.retive(query,10)
CBR.reuse()
print(CBR.r2.predictionCase)














