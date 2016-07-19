#!/usr/bin/env python

import functools
import random


def left_pad(unpadded_string, length, character):
    """
        :param unpadded_string: string to be padded
        :param length: length of the padded string
        :param character: character we must pad the unpadded string with

        Adds :length - len(:unpadded_string) times the character :character
        to the left of :unpadded_string.
    """

    n_chars = length - len(unpadded_string)
    return "{}{}".format(character * n_chars, unpadded_string)


def int_to_bin(integer, digits):
    """
        :param integer: integer to be converted to int
        :param digits: number of digits it must have in its binary representation

        Returns a string with the binary representation of :integer with
        :digits digits.
    """

    bin_str = str(bin(integer)[2:])
    return left_pad(bin_str, digits, "0")


def int_to_bin_array(integer, digits):
    """
        :param integer: integer to be converted to int
        :param digits: number of digits it must have in its binary representation

        Returns a list with the binary representation of :integer
        with length :digits. Each list element is an int.
    """

    return list(map(int, list(int_to_bin(integer, digits))))


def random_solution(size):
    """
        :param size: size of the solution in bits

        Returns a list with the binary representation of a random
        solution with length :size. Each list element is an int.
    """

    solution = random.randrange(2 ** size + 1)
    return int_to_bin_array(solution, size)


def random_mask(mask_size, solution_size):
    """
        :param mask_size: size of the mask to be created
        :param solution_size: size of the solution

        Creates a mask of size :mask_size containing ints from 0 to :solution_size.
    """

    return sorted([random.randrange(solution_size) for _ in range(mask_size)])


def random_players(n, solution_size):
    """
        :param n: number of players to be created
        :param solution_size: number of positions that can be changed in the solution

        Create :n random players. Each player is represented as
        a list of values between 0 and 1 with length :solution_size. Each
        position i of the list contains the probability of changing the i-th value
        of the int list representation of the candidate solution.
    """

    return [[random.random() for _ in range(solution_size)] for _ in range(n)]


def calculate_weight(player, permutation_index, mask):
    """
        :param player: list of probabilities for changing each position of the solution
        :param permuation_index: numerical int index of the permutation
        :param mask: list of integers representing solution positions that can be changed

        Calculates the weight of applying the permutation represented by :permutation_index to
        the mask :mask according to player :player 's own rules.
    """

    mask_active, mask_inactive = mask_transformation(permutation_index, mask)
    active_probs = [player[x] for x in mask_active]
    inactive_probs = [1 - player[x] for x in mask_inactive]
    return functools.reduce(lambda x, y: x * y, active_probs + inactive_probs)


def calculate_rating(players, permutation_index, mask):
    """
        :param player: list of list of probabilities for changing each position of the solution
        :param permutation_index: numerical int representation of the permutation
        :param mask: list of integers representing solution positions that can be changed

        Calculates the rating for permutation :permutation_index according to :players and :mask.
    """

    permutation_weight, total_weight = 0, 0

    for player in players:
        permutation_weight += calculate_weight(player, permutation_index, mask)

        for permutation in range(2 ** len(mask)):
            total_weight += calculate_weight(player, permutation, mask)

    return permutation_weight / total_weight


def mask_transformation(permutation, mask):
    """
        :param permutation: integer index of the permutation
        :param mask: list of integers representing solution positions that can be changed

        Returns the mask indices that are active and the ones that are not active
        based on :permutation and :mask.
    """

    trans = int_to_bin_array(permutation, len(mask))
    active, inactive = [], []
    for allow, solution_position in zip(trans, mask):
        if allow:
            active.append(solution_position)
        else:
            inactive.append(solution_position)

    return active, inactive
