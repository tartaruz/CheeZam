import os

class Tester:
    def __init__(self):
        self.query = None
        self.artist = None
        self.revision = None
        self.first_predict = None
        self.testing = True
        self.case = None
        self.fail_genre = False
        self.fail_subgenre = False

    def setCase(self, case):
        # print(type(case))
        self.case = case
        # sprint(case)

    def search(self):
        self.query="None"
        self.artist="None"
        if self.case.track_name !=None:
            self.query = self.case.track_name.lower()
        if self.case.track_artist != None:
            self.artist = self.case.track_artist.lower()
        return self.query, self.artist

    def consol_print(self, chatCase, prev_predict_correct=None, subgenres=None):
        # os.system('clear')
        if chatCase == "first_predict":
            print(self.case.playlist_genre)
            if (self.case.playlist_genre.lower()==self.revision.reuse.predictionGenre[0].lower()):
                self.first_predict = "y"
            else:
                self.fail_genre = True
                self.first_predict = "n"
            print(f'The CBR-system prediciton: [{self.revision.reuse.predictionGenre[0]}]')
            return self.first_predict 
        elif chatCase == "choose_genre":
            # os.system('clear')
            self.fail_genre = True
            print('Which of the following genres do you think fits the song best?')
            self.revision.genre = self.case.playlist_genre.lower()
            

        elif chatCase == "predict_subgenre":
            # if in voteKNN
            if not len(self.revision.reuse.retrieval.retrievedCases) == 1:
                
                if prev_predict_correct:
                    predictions = [
                        case.playlist_subgenre for case in self.revision.reuse.retrieval.retrievedCases
                        if case.playlist_genre == self.revision.genre.lower()
                    ]
                else:
                    predictions = [
                        case.playlist_subgenre for case in self.revision.reuse.retrieval.retrievedCases
                        if case.playlist_genre != self.revision.genre.lower()
                    ]
                    predictions = self.revision.reuse.genreSort(predictions)[0]
                self.revision.reuse.predictionSubGenre = predictions[0]
                if (predictions[0].lower()==self.case.playlist_subgenre):
                    return "y"
                else:
                    self.fail_subgenre = True
                    return "n"
            else:
                self.revision.reuse.predictionSubGenre = self.revision.reuse.predictionSubGenre[
                    0]
                if self.revision.reuse.predictionSubGenre.lower()==self.case.playlist_subgenre.lower():
                    return "y"
                else:
                    self.fail_subgenre = True
                    return "n"
        elif chatCase == "choose_subgenre":
            # os.system('clear')
            print('Which of the following genres do you think fits the song best?')
            # genres_index = [genre for genre in self.revision.subgenres]
            self.fail_subgenre = True
            return self.case.playlist_subgenre.lower()
            # os.system('clear')
            # if self.case.playlist_subgenre == len(subgenres) + 1:
            #     return input(f'Enter subgenre: ')
            # else:
            #     return subgenres[idx -1]

        else:
            print("Something went wrong")
