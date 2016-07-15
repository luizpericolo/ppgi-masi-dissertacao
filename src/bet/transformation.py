#!/usr/bin/env python

from utils import int_to_bin_array


def get_transformation_mask(n, mask):
    """ returns the mask to be applied to the candidate
    solution taking into account :i and :mask """
    # The strategy chosen was to allow the i-th position
    # of the mask to be modified if :n's i-th digit in
    # binary is 1.

    transformation_mask = []
    n_bin = int_to_bin_array(n, len(mask))

    for mask_element, allow in zip(mask, n_bin):
        if allow:
            transformation_mask.append(mask_element)

    return transformation_mask
