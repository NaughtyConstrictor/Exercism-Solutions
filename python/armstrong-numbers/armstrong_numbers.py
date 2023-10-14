def is_armstrong_number(number: int) -> bool:
    """
    function that checks whether a number is an armestrong number
    """

    if number < 0:
        raise ValueError("number must be a positive integer")
        
    n = str(number)
    len_num = len(n)
    return sum(int(digit)**len_num for digit in n) == number
