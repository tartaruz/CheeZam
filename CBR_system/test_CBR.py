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
        self.file = open("./TheLastTest_retain.txt", "a")
        self.guesses_fail = []



    def test(self, n,voteKNN):
        self.n = n
        cbr = CBR(testing=True)
        # for vote in range(55,65):
        # print((cbr.r1.cases))
        track_ids = [case.track_id for case in cbr.r1.cases]
        self.test_cases = [case for case in self.test_cases if case.track_id not in track_ids]
        for i in range(1,n+1):
            try:
                case = self.test_cases.pop(random.randint(0,len(self.test_cases)-1))
                print(case)
                testObj = Tester()
                testObj.setCase(case)
                if testObj.case != None:
                    cbr.setQuery(tester=testObj)
                    # kNN with K=1  ----> 1-NN
                    cbr.retrieve()
                    # Use the closes neighbor, or have an votation for findng genre data
                    # cbr.r2.voteKNN_nr = vote
                    cbr.reuse()
                    #much fun
                    cbr.revision()        
                    if cbr.user.fail_genre:
                        self.error += 1
                        error = 1
                    else:
                        error = 0
                    
                    cbr.DB.open_connection()
                    cbr.retain() 
                    cbr.DB.close_connection()
                    self.file.write(str(5818-len(self.test_cases)) + "-"+str(self.error) +"-"+str(error)+"-"+str(len(cbr.r1.cases)-len(self.test_cases))+"-"+str(case.track_id)+"\n")
                else:
                    continue
                
                print(str(i) + "-"+str(self.error) +"-"+str((self.error/i)*100)+"-"+str(error)+"-"+str(len(cbr.r1.cases)-len(self.test_cases))+"-"+str(case.track_id)+"\n")
                print(str(5818-len(self.test_cases)) + "-"+str(self.error) +"-"+str(error)+"-"+str(len(cbr.r1.cases)-len(self.test_cases))+"-"+str(case.track_id)+"\n")
                # print(str(vote)+"-"+str(i)+"-"+str(self.error)+"-"+str((self.error/i)*100) +"\n")
                # f.write(str(vote)+"-"+str(i)+"-"+str(self.error)+"-"+str((self.error/i)*100) +"\n")
                # self.error = 0
            except ValueError as e:
                print(e)
                pass
t = Test_CBR()
f = open("./new_vote_distanceAndProbability_NNNNNN.txt", "w")
t.test(len(t.test_cases), 50)