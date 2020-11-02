class Revise:

    def __init__(self, DB):
        # self.genres = ['Pop', 'Rap', 'Rock', 'Latin', 'R&B', 'EDM']
        # self.subgenres = ['dance pop', 'post-teen pop', 'electropop', 'indie poptimism', 'hip hop', 'southern hip hop', 'gangster rap', 'trap', 'album rock', 'classic rock', 'permanent wave', 'hard rock', 'tropical', 'latin pop', 'reggaeton', 'latin hip hop', 'urban contemporary', 'hip pop', 'new jack swing', 'neo soul', 'electro house', 'big room', 'pop edm', 'progressive electro house']
        self.genre = None
        self.subgenre = None
        self.DB = DB
        self.DB.cursor.execute('SELECT DISTINCT playlist_genre FROM cases;')
        self.genres = [genre[0].capitalize() for genre in self.DB.cursor.fetchall()]
        self.DB.cursor.execute('SELECT DISTINCT playlist_subgenre FROM cases;')
        self.subgenres = [subgenre[0].capitalize() for subgenre in self.DB.cursor.fetchall()]

    def revise(self, solution, new_case, artist_genres):
        self.genres += artist_genres
        self.genres = list(set([genre.capitalize() for genre in self.genres]))
        satisfied = input(f'Are you satisfied with the song\'s predicted genre "{solution.playlist_genre}" (y/n)? ')
        print()

        if satisfied.lower() == 'y':
            self.genre = solution.playlist_genre
            self.subgenre = solution.playlist_subgenre

            print('Thank you!')
        else:
            print('Which of the following genres do you think fits the song best?')
            for index, genre in enumerate(self.genres):
                print(f'{index+1}. {genre}')
            print(f'{index+2}. Enter myself')
            
            print()
            ans = int(input(f'1-{index + 2}: '))

            if ans == index+2:
                self.genre = input('Input genre: ')
            else:
                self.genre = self.genres[ans - 1]
            
            want_sub_genre = input('Do you want to provide a sub-genre aswell (y/n)? ')

            if want_sub_genre.lower() == 'y':
                print('Which of the following genres do you think fits the song best?')
                for index, genre in enumerate(self.subgenres):
                    print(f'{index+1}. {genre.capitalize()}')
                print(f'{index+2}. Enter myself')

                print()
                ans = int(input(f'1 - {index + 2}: '))

                if ans == index + 2:
                    self.subgenre = input(f'Enter subgenre: ')
                else:
                    self.subgenre = self.subgenres[ans - 1]
            else:
                self.subgenre = solution.playlist_subgenre

        print()
        print('Thank you for your answers!')

        new_case.setValues(self.genre.lower(), self.subgenre)
        return new_case



        