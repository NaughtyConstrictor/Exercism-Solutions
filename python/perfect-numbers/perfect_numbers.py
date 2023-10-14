from functools import lru_cache, reduce
import math

@lru_cache
def aliquot_sum(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    step = 2 if number % 2 else 1
    stop = 1 + math.isqrt(number - 1)
    initial = stop if stop * stop == number else 0
    return initial + sum(
        reduce(
            list.__add__, 
            ([i, number // i]
             for i in range(1, stop, step)
             if number % i == 0),
            []
        )
    ) - number
    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    sum_ = aliquot_sum(number)
    if sum_ == number:
        return "perfect"
    if sum_ < number:
        return "deficient"
    return "abundant"
