NUMBERS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}

def get_digit(grid: list[str], row_index: int, col_index: int) -> str:
    """
    Returns the digit corresponding to the selected portion of the grid.

    This portion is going to be composed of 4 rows starting from `row_index`
    where each row is going to be 3 columns wide starting from `col_index`.

    Example
    -------
    grid is :
    ' _ '
    '| |' 
    '|_|'
    '   '
    row_index is 0 and col_index is 0
    Should return '0'

    Parameters
    ----------
    grid : list[str]
        A grid of digits represented as strings.
    row_index : int
        Index of the first row of the digit.
    col_index : int
        Index of the first column of the digit.
    
    Returns
    -------
    str
        The digit correspoding to the input as a one character length string.
    """

    number_rows = tuple(
        grid[i][col_index: col_index + 3] for i in range(row_index, row_index + 4)
        )
    return NUMBERS.get(number_rows, "?")


def convert(input_grid: list[str]) -> str:
    """
    Returns the input grid converted to a string of digits.
    
    For more informations check `get_digit()`.

    Parameters
    ----------
    input_grid : list[str]
        A  list of strings containing the rows composing the digits.

    Returns
    -------
    str
        A string of digits correspoding to the input.
    """

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    num_rows = len(input_grid)
    num_cols = len(input_grid[0])
    numbers = [
        "".join(get_digit(input_grid, i, j) for j in range(0, num_cols, 3))
        for i in range(0, num_rows, 4)
    ]

    return ",".join(numbers)
