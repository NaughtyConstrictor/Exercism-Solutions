from collections.abc import Sequence
from typing import Callable, TypedDict

Coordinates = TypedDict("Coordinates", {"row": int, "column": int})


def argmax(sequence: Sequence, key: Callable | None = None) -> list[int]:
    """Returns the indices of all elements equal to `max(sequence)`.

    Parameters
    ----------
    sequence: Sequence
        Input sequence.
    key: Callable, optional
        Callable for comparing items of `sequence` (default is None).

    Returns
    -------
    list[int]
        Indices of all max elements.
    """
    max_ = max(sequence, default=None, key=key)
    if max_ is None:
        return []
    return [index for index, item in enumerate(sequence) if item == max_]


def argmin(sequence: Sequence, key: Callable | None = None) -> list[int]:
    """Returns the indices of all elements equal to `min(sequence)`.

    Parameters
    ----------
    sequence: Sequence
        Input sequence.
    key: Callable, optional
        Callable for comparing items of `sequence` (default is None).

    Returns
    -------
    list[int]
        Indices of all min elements.
    """
    min_ = min(sequence, default=None, key=None)
    if min_ is None:
        return []
    return [index for index, item in enumerate(sequence) if item == min_]


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

    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("irregular matrix")

    answers = []
    candidate_columns = {
        (row_index, col_index) 
        for row_index, row in enumerate(matrix)
        for col_index in argmax(row)
    }
    candidate_rows = {
        (row_index, col_index) 
        for col_index, column in enumerate(transpose(matrix))
        for row_index in argmin(column)
    }

    return [
        dict(row=row + 1, column=col + 1)
        for row, col in candidate_rows & candidate_columns
    ]
    