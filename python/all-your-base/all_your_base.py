def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Converts a number from one base to another
    
    Parameters
    ----------
    intput_base:
        The base of the number to be converted, must be greater than or equal to 2
    digits:
        The digits of the number to be converted
    output_base:
        The base of the number after conversion, must be greater than or equal to 2

    Returns
    -------
    A list of the digits of the number after conversion

    Raises
    ------
    ValueError
        If input base or output base are less than 2
        If the digits of the number are not valid: not in range [0, input_base)
        
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(not 0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if input_base == output_base:
        return digits
        
    in_decimal = sum(
        digit * input_base**i
        for i, digit in enumerate(reversed(digits))
    )
        
    converted = []
    while in_decimal:
        in_decimal, remainder = divmod(in_decimal, output_base)
        converted.append(remainder)

    return converted[::-1] if converted else [0]
    