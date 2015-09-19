#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sometimes cats."""


def too_many_kittens(kittens, litterboxes, catfood):
    """ Calculates if there are too many kittens.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        catood (bool): Wether or not there's catfood

    Returns:
        Statement that ensures we have at least 1 litterbox/catfood per kitten.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    print (not (litterboxes >= kittens and catfood))
