from main import CBR
from model.case import case
from help_modules.tester import Tester
from server.DB import DbConnector
import random

class Test_CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.DB.cursor.execute("SELECT * FROM test_cases")
        res = self.DB.cursor.fetchall()
        self.test_cases =[case(data) for data in res]
        self.n, self.error = 0,0
        self.file = open("./log_no_dur.txt", "w")

    def test(self, n):
        self.n = n
        cbr = CBR(testing=True)
        for i in range(1,n+1):
            case = self.test_cases.pop(random.randint(0,len(self.test_cases)))
            print(case)
            testObj = Tester()
            testObj.setCase(case)
            if testObj.case != None:
                cbr.setQuery(tester=testObj)
                # kNN with K=1  ----> 1-NN
                cbr.retrieve()
                # Use the closes neighbor, or have an votation for findng genre data
                cbr.reuse()
                #much fun
                cbr.revision()        
                if cbr.user.fail_genre:
                    self.error += 1
                self.file.write(str(i) + "-"+str(self.error) +"-"+str((self.error/i)*100)+"\n")
            else:
                pass
            print(i, self.error, (self.error/i)*100)
t = Test_CBR()
t.test(1500)