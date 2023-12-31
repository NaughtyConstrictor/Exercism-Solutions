from collections import Counter
import re


def count_words(sentence: str) -> dict[str, int]:
    return Counter(re.findall(
        r"([a-z0-9]+'[a-z0-9]+|[a-z0-9]+)", 
        sentence.lower()
        )
    )
    