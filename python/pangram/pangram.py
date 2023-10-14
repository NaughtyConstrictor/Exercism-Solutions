import string

def is_pangram(sentence):
    """Returns if a sentence is a pangram."""

    if len(sentence) < 26:
        return False

    return set(string.ascii_lowercase).issubset(sentence.lower())