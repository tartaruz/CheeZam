from server.DB import DbConnector
from Retrieval import Retrieval
from Reuse import Reuse


class CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse()














