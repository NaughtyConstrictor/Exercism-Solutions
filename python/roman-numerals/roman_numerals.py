def _make_roman_numerals(lower: str, middle: str, upper: str) -> list[str]:
    """Helper function for creating the list of roman digits for the hundreds,
    tens and ones.
    """
    return (
        [""]                                   +
        [lower * i for i in range(1, 4)]       +
        [lower + middle]                       +
        [middle + lower * i for i in range(4)] +
        [lower + upper]
    )

    
THOUSANDS = [""] + ["M" * i for i in range(1, 4)]
HUNDREDS = _make_roman_numerals("C", "D", "M")
TENS = _make_roman_numerals("X", "L", "C")
ONES = _make_roman_numerals("I", "V", "X")


def roman(number: int) -> str:
    """Converts a normal number to a roman numeral."""
    answer = ""
    for digit, roman_numeral in zip(str(number).zfill(4), (THOUSANDS, HUNDREDS, TENS, ONES)):
        answer += roman_numeral[int(digit)]
    return answer
    