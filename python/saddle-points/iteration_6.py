# using inclusion exclusion principle
from itertools import combinations
from math import lcm


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    sums = []
    multiples = list(filter(None, multiples))
    for i in range(1, len(multiples) + 1):
        temp_sum = []
        for intersection in combinations(multiples, r=i):
            multiple = lcm(*intersection)
            n = (limit + multiple - 1) // multiple - 1
            s = multiple * ( ((n + 1 )*n) // 2)
            temp_sum.append(s)
        temp_sum = sum(temp_sum) * (1 if i % 2 else -1)
        sums.append(temp_sum)
    return sum(sums)