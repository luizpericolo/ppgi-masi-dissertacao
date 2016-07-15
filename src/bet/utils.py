#!/usr/bin/env python


def left_pad(element, length, character):
    """ adds :length - len(:element) times the character :character
    to the left of :element """

    n_chars = length - len(element)
    return "{}{}".format(character * n_chars, element)


def int_to_bin(integer, digits):
    """ returns a string with the binary representation of :integer with
    :digits digits """

    bin_str = str(bin(integer)[2:])
    return left_pad(bin_str, digits, "0")


def int_to_bin_array(integer, digits):
    """ returns a list with the binary representation of :integer
        with length :digits. Each list element is an int """

    return list(map(int, list(int_to_bin(integer, digits))))
