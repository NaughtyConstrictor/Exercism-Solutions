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
    for i, row in enumerate(matrix):
        candidate_columns = argmax(row)

        # unnecessary check since a max is guaranteed to exist
        # if not candidate_columns:
        #     continue

        for candidate_column in candidate_columns:
            column = [row[candidate_column] for row in matrix]
            candidate_rows = argmin(column)
            for candidate_row in candidate_rows:
                if candidate_row == i:
                    answers.append(
                        {
                            "row": candidate_row + 1, 
                            "column": candidate_column + 1
                        }
                    )
                    
    return answers
    