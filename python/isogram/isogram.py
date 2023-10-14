def is_isogram(string):
    """Returns if string is an isogram."""

    flag = 0b11111111111111111111111111
    state = 0
    for char in string:
        char = ord(char.lower()) - ord('a')
        if not 0 <= char < 26:
            continue
        position = 1 << char
        if state & position:
            return False
        state |= position
        
    return True