def leap_year(year):
    """
    function to return if a year is a leap year 
    """

    if not isinstance(year, int):
        raise TypeError("year must be a whole number")
    
    if year < 0:
        raise ValueError("year can't be negative")

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)