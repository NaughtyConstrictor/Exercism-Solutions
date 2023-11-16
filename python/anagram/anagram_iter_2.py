from collections import Counter

def is_anagram(str_1: str, str_2: str) -> bool:
    """Returns if str_1 and str_2 are anagrams."""
    return str_1 != str_2 and Counter(str_1) == Counter(str_2)    

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Returns set of all anagrams of word present in candidates

    Parameters
    ----------
    word:
        The word to check for its anagrams.
    candidates:
        List of candidate anagrams.

    Returns
    -------
    List of the inputs' anagrams from candidates.    
    """

    word = word.lower()
    return [
        candidate 
        for candidate in candidates 
        if is_anagram(word, candidate.lower())
    ]