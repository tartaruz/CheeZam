class Retain:

    def __init__(self, DB):
        self.case = None
        self.DB = DB
    
    def setCase(self,case):
        self.case = case

    def retain(self):
        if self.case != None:
            self.DB.cursor.execute(self.case.toDict())
        else:
            return Exception("No case to retain")
    