from collections.abc import Sequence
from typing import Callable, TypedDict


Coordinates = TypedDict("Coordinates", {"row": int, "column": int})


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Returns the transpose of a matrix"""
    return list(zip(*matrix))


def saddle_points(matrix: list[list[int]]) -> list[Coordinates]:
    """Returns coordinates of all saddle points.

    A saddle point is:
    - greater than every point to the east and west.
    - shorter than every point to the north and south.

    Parameters
    ----------
    matrix: list[list[int]]
        Matrix of points
    
    Returns
    -------
    list[Coordinates]
        List of all saddle points coordinates.
    """
    if not matrix:
        return []

    height = len(matrix)
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("irregular matrix")

    answers = []
    matrix_t = transpose(matrix)
    for i, row in enumerate(matrix):
        for j, col in zip(range(width), matrix_t):
            current = matrix[i][j]
            is_max_col = all(
                current >= value for k, value in enumerate(row) if k != j
            )
            if not is_max_col:
                continue
            is_min_row = all(
                current <= value for k, value in enumerate(col) if k != i
            )
            if not is_min_row:
                continue
            answers.append((i, j))
    
    return [
        dict(row=row + 1, column=col + 1)
        for row, col in answers
    ]
    