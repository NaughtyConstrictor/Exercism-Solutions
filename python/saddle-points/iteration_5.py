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

    matrix_t = transpose(matrix)
    # checks if a value is the max in of column
    # all(matrix[i][j] >= value for k, value in enumerate(row) if k != j)
    # checks if a value is the min of a row
    # all(matrix[i][j] <= value for k, value in enumerate(col) if k != i)
    
    coordinates = [
        (i, j)
        for i, row in enumerate(matrix)
        for j, col, current in zip(range(width), matrix_t, row)
        if (
            all(current >= value for k, value in enumerate(row) if k != j) and 
            all(current <= value for k, value in enumerate(col) if k != i)
        )
    ]
     
    return [
        dict(row=row + 1, column=col + 1)
        for row, col in coordinates
    ]
    