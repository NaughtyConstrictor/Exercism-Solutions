def is_valid(isbn):
    """Returns if an isbn is valid."""

    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    isbn = list(isbn)
    if isbn[-1] == "X":
        isbn[-1] = "10"
    if not all(digit.isdecimal() for digit in isbn):
        return False
    return sum(int(digit)*(10 - i) for i, digit in enumerate(isbn)) % 11 == 0
    