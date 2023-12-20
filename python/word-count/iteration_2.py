import string


SEPARATORS = string.punctuation + string.whitespace
SEPARATORS_NO_APOSTROPHE = SEPARATORS.replace("'", "")
TRANSLATION_TABLE = str.maketrans(
    SEPARATORS_NO_APOSTROPHE, " " * len(SEPARATORS_NO_APOSTROPHE)
)


def count_words(sentence: str) -> dict[str, int]:
    counts = {}
    sentence = sentence.strip(SEPARATORS)
    sentence = sentence.translate(TRANSLATION_TABLE)
    for word in sentence.split():
        word = word.strip(string.punctuation).casefold()
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts
    