def annotate(minefield: list[str]) -> list[str]:
    """Returns the minefield with the mine counts.

    Each empty square will be replaced with the count of mines that are directly
    adjacent to it (horizontally, vertically, diagonally).

    Parameters
    ----------
    minefield:
        The minefield as a list of strings. The strings must contain any combination 
        of blank spaces (' ') and asterisk ('*'). (A mine is represented by the               asterisk).

    Returns
    -------
    The new minfield with empty squares replaced with their respective count for          adjacent mines.

    Raises
    ------
    ValueError:
        If the input is invalid (the minefield contains characters other than 
        ` ` and `*`).
    """

    if minefield == [] or minefield == [""]:
        return minefield

    len_row = len(minefield[0])
    if any(len(row) != len_row or set(row) - {" ", "*"} for row in minefield):
        raise ValueError("The board is invalid with current input.")

    board = ["".join(["#", row, "#"]) for row in minefield]
    board = ["#" * (len_row + 2), *board, "#" * (len_row + 2)]

    return [
        "".join([
            str("".join([
                board[i - 1][j-1:j+2],
                board[i][j-1:j+2],
                board[i + 1][j-1:j+2],
            ]).count("*")).replace("0", " ")
            if board[i][j] == " " else "*"
            for j in range(1, len_row + 1)
        ])
        for i in range(1, len(minefield) + 1)
    ]

