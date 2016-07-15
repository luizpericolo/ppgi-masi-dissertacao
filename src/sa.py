import math
from random import random, uniform

from sa_functions import mapping


def random_solution(x_bounds, y_bounds):
    x_low, x_high = x_bounds
    y_low, y_high = y_bounds

    return uniform(x_low, x_high), uniform(y_low, y_high)


def neighbor(solution):
    # XXX: Fix neighbor function
    x, y = solution
    x_off, y_off = uniform(-1, 1), uniform(-1, 1)

    return x + x_off, y + y_off


def acceptance_probability(old_cost, new_cost, T):
    return math.exp((new_cost - old_cost) / T)


def anneal(solution, cost):
    old_cost = cost(*solution)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_solution = neighbor(solution)
            new_cost = cost(*new_solution)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                solution = new_solution
                old_cost = new_cost
            i += 1
        T = T * alpha
    return solution, old_cost

if __name__ == "__main__":

    for func, func_info in mapping.items():
        print(func.__name__)
        x_domain, y_domain = func_info.get("domain")

        initial_solution = random_solution(x_domain, y_domain)

        print(x_domain, y_domain)
        print(initial_solution)
        print()

        solution, old_cost = anneal(initial_solution, cost=func)

        print("solution is: {}".format(solution))
