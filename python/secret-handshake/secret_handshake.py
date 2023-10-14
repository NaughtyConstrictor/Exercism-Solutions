ACTIONS = [
    "wink",
    "double blink", 
    "close your eyes", 
    "jump",
]

def commands(binary_str: str) -> list[str]:
    """Returns the sequence of actions corresponding to the input

    Parameters
    ----------
    binary_str:
        A string containing binary digits.

    Returns
    -------
    A list containing the series of actions corresponding to the input.
    """

    reverse, *digits = binary_str
    actions = [
        ACTIONS[i]
        for i, digit in enumerate(reversed(digits))
        if digit == "1"
    ]

    if reverse == "1":
        return actions[::-1]
    return actions