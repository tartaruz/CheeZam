class Revise:

    def __init__(self, DB):
        # self.genres = ['Pop', 'Rap', 'Rock', 'Latin', 'R&B', 'EDM']
        # self.subgenres = ['dance pop', 'post-teen pop', 'electropop', 'indie poptimism', 'hip hop', 'southern hip hop', 'gangster rap', 'trap', 'album rock', 'classic rock', 'permanent wave', 'hard rock', 'tropical', 'latin pop', 'reggaeton', 'latin hip hop', 'urban contemporary', 'hip pop', 'new jack swing', 'neo soul', 'electro house', 'big room', 'pop edm', 'progressive electro house']
        self.reuse = None
        self.case = None
        self.genre = None
        self.subgenre = None
        self.DB = DB
        self.DB.cursor.execute('SELECT DISTINCT playlist_genre FROM cases;')
        self.genres = [genre[0].capitalize()
                       for genre in self.DB.cursor.fetchall()]
        self.DB.cursor.execute('SELECT DISTINCT playlist_subgenre FROM cases;')
        self.subgenres = [subgenre[0].capitalize()
                          for subgenre in self.DB.cursor.fetchall()]

    def revise(self):
        # CBR, new_case, artist_genres
        self.genres = list(set([genre.capitalize() for genre in self.genres]))

        answer = self.consol_print("first_predict")
        print()

        # If correct prediciton
        if answer.lower() == 'y':
            self.genre = self.reuse.predictionGenre[0]
        # If incorrect, predict new genre
        else:
            ans = self.consol_print("choose_genre")

        satisfied = self.consol_print(
            "predict_subgenre", (answer.lower() == 'y'))

        if satisfied.lower() == 'y':
            self.subgenre = self.reuse.predictionSubGenre
        else:
            ans = self.consol_print("choose_subgenre")
            if ans == len(self.subgenres) + 2:
                self.subgenre = input(f'Enter subgenre: ')
            else:
                self.subgenre = self.subgenres[ans - 1]

        print()
        print('Thank you for your answers!')

        # Update the case to predicitons or decitions
        self.case.playlist_genre = self.genre
        self.case.playlist_subgenre = self.subgenre


    def consol_print(self, chatCase, prev_predict_correct=None):
        if chatCase == "first_predict":
            return input(f'Are you satisfied with the song\'s predicted genre "{self.reuse.predictionGenre[0]}" (y/n)? ')

        elif chatCase == "choose_genre":
            print('Which of the following genres do you think fits the song best?')
            if len(self.reuse.genres) == 1:
                for index, genre in enumerate(self.genres):
                    print(f'{index+1}. {genre}')
                print(f'{index+2}. Enter myself')
                print()
                idx = int(input(f'1-{index + 2}: '))

                if idx == len(self.genres)+2:
                    self.genre = input('Input genre: ')
                else:
                    print()
                    self.genre = self.genres[idx - 1].lower()
            else:
                for index, genre in enumerate(self.reuse.genres):
                    print(f'{index+1}. {genre[0].title()}')
                print(f'{index+2}. Enter myself')
                print()
                idx = int(input(f'1-{index + 2}: '))

                if idx == len(self.reuse.genres)+2:
                    self.genre = input('Input genre: ')
                else:
                    print()
                    self.genre = self.reuse.genres[idx - 1][0]

        elif chatCase == "predict_subgenre":
            # if in voteKNN
            if not len(self.reuse.retrieval.retrievedCases) == 1:
                if prev_predict_correct:
                    predictions = [
                      case.playlist_subgenre for case in self.reuse.retrieval.retrievedCases 
                        if case.playlist_genre == self.genre.lower()
                    ]
                else:
                    predictions = [
                        case.playlist_subgenre for case in self.reuse.retrieval.retrievedCases 
                            if case.playlist_genre != self.genre.lower()
                        ]
                    predictions = self.reuse.genreSort(predictions)[0]
                self.reuse.predictionSubGenre = predictions[0]
                return input(f'Are you satisfied with the song\'s predicted sub-genre "{predictions[0]}" (y/n)? ')
            else:
                self.reuse.predictionSubGenre = self.reuse.predictionSubGenre[0]
                return input(f'Are you satisfied with the song\'s predicted sub-genre "{self.reuse.predictionSubGenre}" (y/n)? ')

        elif chatCase == "choose_subgenre":
            print('Which of the following genres do you think fits the song best?')
            for index, genre in enumerate(self.subgenres):
                print(f'{index+1}. {genre.capitalize()}')
            print(f'{index+2}. Enter myself')

            print()
            idx = int(input(f'1 - {index + 2}: '))
            return idx

        else:
            print("Something went wrong")
