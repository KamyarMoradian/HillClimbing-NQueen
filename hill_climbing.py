def hill_climbing(problem):
    """ Returns a state as the solution of the problem """
    state = problem.initial()
    while True:
        if problem.goal_test(state):
            return state
        neighbors = problem.neighbors(state)
        if not neighbors:
            return state
        neighbor = min(neighbors, key=problem.value)
        if problem.value(neighbor) >= problem.value(state):
            return state
        state = neighbor


def hill_climbing_random_restart(problem, limit=10):
    state = problem.initial()
    cnt = 0
    while not problem.goal_test(state) and cnt < limit:
        state = hill_climbing(problem)
        cnt += 1
    return state
