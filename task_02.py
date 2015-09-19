#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""

import hamlet


def crazy_math(monkeys, hours, typewriters=None, bananas=None):
    """ Calculates the chance creating Hamlet based on number of monkeys,
        bananas, typewriters, and hours.

        There would be a paragraph here, should there be a necessity.

        Args:
            monkeys (int): Number monkeys available.
            hours (mixed): Number of hours available.
            typewriters (int): Number of typewriters avaliable;
                default is set to None.
            bananas (int): Number of avaliable bananas, by default None

        Returns:
            float: Chance of successfuly writing up Hamlet using this method.

        Examples:

            >>> import task_02
            >>> print task_02.POSITIONAL
            0.00374391674995
    """
    myvar = hamlet.crazy_math(4, 100000, 8, 98)
    return myvar


POSITIONAL = crazy_math(4, 1000000, 8, 98)
