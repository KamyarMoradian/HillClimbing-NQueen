from random import randrange


class NQueens:
    def __init__(self, N):
        self.N = N

    def initial(self):
        ''' Returns a random initial state '''
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        ''' Returns True if the given state is a goal state '''

    def value(self, state):
        ''' Returns the value of a state. The higher the value, the closest to a goal state '''

    def neighbors(self, state):
        ''' Returns all possible neighbors (next states) of a state '''
