def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Returns `legacy_data` in the new data format or letters and their corresponding
    point values

    `legacy_data` format is: {point_value: [letter_1, letter_2, ...]}
    new data format is: {letter_1: point_value, letter_2: point_value, ...}
    
    Example of `legacy_data` format:
    {
        1: ["A", "B"],
        2: ["C"],
        ...
    }
    New data format is the following:
    {
        "a": 1,
        "b": 1,
        "c": 2
        ...
    }

    Parameters
    __________
    legacy_data: dict[int, list[str]]
        Legacy data in the format described above.

    Returns
    _______
    dict[str, int]
        Legacy data in the new data format, as described above.
    """
    return {
        letter.lower(): point
        for point, letters in legacy_data.items()
        for letter in letters
    }

    
# def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
#     new_data = {}
#     for point, letters in legacy_data.items():
#         for letter in letters:
#             new_data[letter.lower()] = point
#     return new_data
