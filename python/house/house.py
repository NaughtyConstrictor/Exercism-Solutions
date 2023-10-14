VERSES = [
    'that lay in the house that Jack built', 
    'that ate the malt', 
    'that killed the rat', 
    'that worried the cat', 
    'that tossed the dog', 
    'that milked the cow with the crumpled horn', 
    'that kissed the maiden all forlorn', 
    'that married the man all tattered and torn', 
    'that woke the priest all shaven and shorn', 
    'that kept the rooster that crowed in the morn', 
    'that belonged to the farmer sowing his corn', 
    'the horse and the hound and the horn'
]

def recite_verse(verse: int) -> str:
    """Returns the nursery rythme corresponding to the verse number."""
    
    if verse == 1:
        return "This is the house that Jack built."

    first_sentence = VERSES[verse - 1]
    start = first_sentence.find("the")
    return (
        "This is " + 
        first_sentence[start:] + " " +
        " ".join(VERSES[verse - 2::-1]) + 
        "."
    )


def recite(start_verse: int, end_verse: int) -> str:
    """Returns a list of nursery rythmes corresponding to versees from 
    start_verse to end_verse."""
    
    return [
        recite_verse(verse)
        for verse in range(start_verse, end_verse + 1)
    ]
