class Revise:
    def revise(self, solution, new_case):
        satisfied = input('Are you satisfied with the song\'s predicted genre (y/n)? ')

        if satisfied.lower() == 'y':
            return True
        