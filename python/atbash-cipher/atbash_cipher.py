import string


ENCODER = str.maketrans(
    string.ascii_lowercase, 
    string.ascii_lowercase[::-1],
    string.whitespace + string.punctuation
)

def encode(plain_text: str) -> str:
    """Returns the input encoded using the Atbash cipher

    Only alphabetic characters will be considered, i.e spaces, punctuation ... 
    will be ignored.
    The encoded message will be in lowercase, in groups of 5 letters separated by a space.
    
    Parameters
    ----------
    plain_text:
        The message to be incoded.

    Returns
    -------
    The encoded message using the Atabash cipher.
    """

    ciphered_text = plain_text.lower().translate(ENCODER)
    return " ".join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))

def decode(ciphered_text: str) -> str:
    """Returns the input decoded using the Atbash cipher

    Parameters
    ----------
    ciphered_text:
        The message to be decoded.

    Returns
    -------
    The decoded message using the Atabash cipher.
    """

    return ciphered_text.translate(ENCODER)