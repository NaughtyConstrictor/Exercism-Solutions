def rows(letter: str) -> str:
    if letter == "A":
        return [letter]
    levels = ord(letter) - ord("A") - 1
    result = [" " * (levels + 1) + "A" + " " * (levels + 1)]
    for level in range(levels, -1, -1):
        space = " " * level
        middle = " " * (2 * (levels - level) + 1)
        l = chr(ord(letter) - level)
        result.append(space + l + middle + l + space)
    result.extend(result[levels::-1])
    return result