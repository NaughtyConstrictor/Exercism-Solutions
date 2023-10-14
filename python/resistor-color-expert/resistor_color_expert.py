COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCE = {
    "grey":     0.05,
    "violet":   0.1,
    "blue":     0.25,
    "green":    0.5,
    "brown":    1,
    "red":      2,
    "gold":     5,
    "silver":   10,
}

UNIT_PREFIX = {
    1_000_000_000:    "giga",
    1_000_000:        "mega",
    1_000:            "kilo",
}

def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return _one_band_resistor(colors[0])
    elif len(colors) == 4 or len(colors) == 5:
        return _band_resistor(colors)
    else:    
        raise ValueError("You must supply 1, 4 or 5 colors")

def _one_band_resistor(color: str) -> str:
    """Helper function for a one band resistor

    The function essentially returns the string `0 ohms` for the color `black`
    
    Parameters
    ----------
    color:
        Color name, must be `black`.

    Returns
    -------
    The string `0 ohms`.

    Raises
    ------
    ValueError:
        If the color supplied is not `black`.
    """
    
    if color != "black":
        raise ValueError("Invalid one band resistor color: can only be `black`")

    return "0 ohms"

def _band_resistor(colors: list[str]) -> str:
    *colors, tolerance = colors
    tolerance = TOLERANCE.get(tolerance)
    if tolerance is None:
        raise ValueError("Invalid tolerance color")

    if any(color not in COLORS for color in colors):
        raise ValueError("Invalid color name")

    *digits, num_zeros = map(COLORS.get, colors)
    n = len(digits)
    resistance_value = sum(
        digit * 10**(n - i) 
        for i, digit in enumerate(digits, start=1)
    ) * 10**num_zeros

    return f"{format_unit_prefix(resistance_value)}ohms ±{tolerance}%"

def format_unit_prefix(value: [int, float]) -> str:
    """Returns the input with the corresponding unit prefix

    For example: input=`1000`, output=`1 kilo`
    
    Parameters
    ----------
    value:
        A number to be formated.

    Returns
    -------
    The formatted value with the corresponding prefix.
    """

    for limit, prefix in UNIT_PREFIX.items():
        if value >= limit:
            value = value / limit if value % limit else value // limit
            return f"{value} {prefix}"

    return f"{value} "