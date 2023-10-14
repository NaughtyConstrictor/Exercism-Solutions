import itertools


def steps(number: int) -> int:
    """Return the number of steps of a collatz sequence."""

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    for num_steps in itertools.count():
        if number == 1:
            break
        if number % 2:
            number = 3 * number + 1
        else:
            number //= 2
    return num_steps