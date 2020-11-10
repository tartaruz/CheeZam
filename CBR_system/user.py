import os

class User:
    def __init__(self):
        self.query = None
        self.artist = None
        self.revision = None
        self.first_predict = None

    def search(self):
        self.query = input(
            'Please input a song title to predict genre: ').lower()
        self.artist = input('Please enter artist of the song: ').lower()
        return self.query, self.artist

    def consol_print(self, chatCase, prev_predict_correct=None, subgenres=None):
        # os.system('clear')
        if chatCase == "first_predict":
            self.first_predict = input(f'The CBR-system prediciton: [{self.revision.reuse.predictionGenre[0]}]\nAre you satisfied with the song\'s predicted genre "{self.revision.reuse.predictionGenre[0]}" (y/n)? ')
            return self.first_predict
        elif chatCase == "choose_genre":
            # os.system('clear')
            print('Which of the following genres do you think fits the song best?')
            if len(self.revision.reuse.genres) == 1:
                for index, genre in enumerate(self.revision.genres):
                    print(f'{index+1}. {genre}')
                print(f'{index+2}. Enter myself')
                print()
                idx = int(input(f'1-{index + 2}: '))

                if idx == len(self.revision.genres)+2:
                    self.revision.genre = input('Input genre: ')
                else:
                    print()
                    self.revision.genre = self.revision.genres[idx - 1].lower()
            else:
                # genre_options = [case[0].capitalize() for case in self.revision.reuse.genres if case[0].capitalize()!="Latin"]
                # [genre_options.append(case) for case in self.revision.genres if case not in self.revision.genres]
                # print(genre_options)
                for index, genre in enumerate(self.revision.reuse.genres):
                    print(f'{index+1}. {genre[0].title()}')
                print(f'{index+2}. Enter myself')
                print()
                idx = int(input(f'1-{index + 2}: '))

                if idx == len(self.revision.reuse.genres)+1:
                    self.revision.genre = input('Input genre: ')
                else:
                    print()
                    self.revision.genre = self.revision.reuse.genres[idx - 1][0]

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
                return input(f'Are you satisfied with the song\'s predicted sub-genre "{predictions[0]}" (y/n)? ')
            else:
                self.revision.reuse.predictionSubGenre = self.revision.reuse.predictionSubGenre[
                    0]
                return input(f'Are you satisfied with the song\'s predicted sub-genre "{self.revision.reuse.predictionSubGenre}" (y/n)? ')

        elif chatCase == "choose_subgenre":
            # os.system('clear')
            print('Which of the following genres do you think fits the song best?')
            for index, genre in enumerate(self.revision.subgenres):
                print(f'{index+1}. {genre.capitalize()}')
            print(f'{index+2}. Enter myself')

            print()
            idx = int(input(f'1 - {index + 2}: '))
            # os.system('clear')
            if idx == len(subgenres) + 1:
                return input(f'Enter subgenre: ')
            else:
                return subgenres[idx -1]

        else:
            print("Something went wrong")
