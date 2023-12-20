from collections import Counter
import string

SEPARATORS = string.punctuation + string.whitespace
SEPARATORS_NO_APOSTROPHE = SEPARATORS.replace("'", "")
TRANSLATION_TABLE = str.maketrans(
    SEPARATORS_NO_APOSTROPHE,
    " " * len(SEPARATORS_NO_APOSTROPHE)
)


def count_words(sentence: str) -> dict[str, int]:
    sentence = sentence.strip(SEPARATORS).translate(TRANSLATION_TABLE)
    words = [word.strip(SEPARATORS).casefold() for word in sentence.split()]
    return Counter(words)
