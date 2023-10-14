"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import List

# Possible sublist categories.
# Change the values as you see fit.
UNEQUAL = 0
SUBLIST = 1
EQUAL = 2
SUPERLIST = 3


def sublist(list_one: List[int], list_two: List[int]) -> int:
    """Returns the relationship of list_one with respect to list_two

    The relationship is determined as follows:
    list_one is equal to list_two if 
        both lists have the same values in the same order.
    list_one is a superlist of list_two if
        list_one contains a sub-sequence of values equal to list_two.
    list_one is a sublist of list_two if
        list_two contains a sub-sequence of values equal to list_one.
    If none of the above then the two lists are considered unequal.
    """

    if list_one == list_two:
        return EQUAL

    list_one = "".join("-" + str(item) + "-" for item in list_one)
    list_two = "".join("-" + str(item) + "-" for item in list_two)

    if list_one in list_two:
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    return UNEQUAL
    