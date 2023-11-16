def is_armstrong_number(number):
    """
    function that checks whether a number is an armestrong number
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if number < 0:
        raise ValueError("number must be a positive integer")
        
    n = str(number)
    len_num = len(n)
    sum_ = 0
    for digit in n:
        sum_ +=  int(digit)**len_num
        if sum_ > number:
            return False
    return sum_ == number