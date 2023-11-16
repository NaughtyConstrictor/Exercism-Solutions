def find(search_list: list[int], value: int) -> int:
    left = 0
    right = len(search_list) - 1
    while left <= right:
        middle = left + (right - left) // 2
        element = search_list[middle]
        if element == value:
            return middle
        elif element > value:
            right = middle - 1
        else:
            left = middle + 1
    raise ValueError("value not in array")