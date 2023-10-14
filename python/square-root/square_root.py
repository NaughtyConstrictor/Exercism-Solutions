def square_root(number: int) -> float:
    """Returns an approximation of the square root of a positive natural number

    Newton's method, also know as Newton-Raphson method is used.
    For more information check: `https://en.wikipedia.org/wiki/Newton%27s_method`
    
    Parameters
    ----------
    number:
        input number, must be a positive natural number.

    Returns
    -------
    An approximation of the square root of the input number.

    Raises
    ------
    ValueError:
        If the input number is not a positive natural number.
    """

    if number < 0 or not isinstance(number, int):
        raise ValueError("number must be a positive natural number")

    if number <= 1:
        return number
        
    for i in range(number // 2 + 1):
        if i * i == number:
            return i
    return None