#! /usr/bin/env python

import random
from functools import partial

from utils import int_to_bin_array, left_pad

SOLUTION_SIZE = 5
MASK_SIZE = 3

binary_padder = partial(left_pad, character="0")


def create_players(n, solution_size=SOLUTION_SIZE):
    """ create :n random players. Each player is represented as
    a list of values between 0 and 1 with length :solution_size. Each
    position i of the list contains the probability of changing the i-th value
    of the int list representation of the candidate solution. """

    return [[random.random() for _ in range(solution_size)] for _ in range(n)]


def create_random_solution(solution_size=SOLUTION_SIZE):
    """ creates a random solution with :solution_size digits. It is
    represented as an int list """

    random_solution = random.randrange(2 ** solution_size)
    return int_to_bin_array(random_solution, solution_size)


def create_mask(mask_size=MASK_SIZE, solution_size=SOLUTION_SIZE):
    """ creates a mask of size :mask_size containing ints from 0 to :solution_size """

    return sorted([random.randrange(solution_size) for _ in range(mask_size)])
