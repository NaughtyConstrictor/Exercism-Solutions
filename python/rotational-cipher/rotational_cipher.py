def _rotate_letter(letter, key):
    if not letter.isalpha():
        return letter
    
    offset = ord("A") if letter.isupper() else ord("a")
    letter = ord(letter)
    return chr(offset + (letter - offset + key) % 26)
    
def rotate(text: str, key: int) -> str:
    """Returns the rotational (Caesar) cipher of text."""

    if not 0 <= key <= 26:
        raise ValueError("Key must be in range 0 - 26")

    if key == 0 or key == 26:
        return text

    return "".join(_rotate_letter(char, key) for char in text)
    