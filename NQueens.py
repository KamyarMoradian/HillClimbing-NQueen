from random import randrange


class NQueens:
    def __init__(self, dim):
        self.dim = dim

    def initial(self):
        """ Returns a random initial state """
        return tuple(randrange(self.dim) for i in range(self.dim))

    def goal_test(self, state):
        """ Returns True if the given state is a goal state """
        return self.value(state) == 0

    def value(self, state):
        """ Returns the value of a state. The higher the value, the closest to a goal state """
        cnt = 0
        for i in range(self.dim):
            cnt += self.check_col(state, i, state[i])
            cnt += self.check_diag(state, i, state[i])
        return cnt / 2

    def check_col(self, state, row, col):
        """ Returns the number of conflicts in a column """
        cnt = 0
        for i in range(self.dim):
            if i != row and state[i] == col:
                cnt += 1
        return cnt

    def check_diag(self, state, row, col):
        """ Returns the number of conflicts in a diagonal """
        cnt = 0
        for i in range(self.dim):
            if i != row and abs(state[i] - col) == abs(i - row):
                cnt += 1
        return cnt

    def neighbors(self, state):
        """ Returns all possible neighbors (next states) of a state """
        next_states = []
        for i in range(self.dim):
            for j in range(self.dim):
                if j != state[i]:
                    next_state = list(state)
                    next_state[i] = j
                    next_states.append(tuple(next_state))
        return next_states
