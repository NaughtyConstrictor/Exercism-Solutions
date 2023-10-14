def encode_integer(number: int) -> list[int]:
    """Returns the vlq encoding for a 32-bit unsigned integer

    For more information check: 
    `https://en.wikipedia.org/wiki/Variable-length_quantity`
    
    Parameters
    ----------
    number:
        A 32-bit unsigned integer to be encoded using vlq encoding.

    Returns
    -------
    The vlq encoding of the input number.

    Raises
    ------
    ValueError:
        If the input number isn't a 32-bit unsigned integer.
    """

    # max_unsigned_int32 = 2**32 - 1 = 4294967295
    if not 0 <= number <= 4294967295:
        raise ValueError("number isn't a valid 32-bit unsigned integer")
    
    if number == 0:
        return [0]
    
    mask = 0b1111111
    msb_mask = 0b10000000
    bytes_ = []
    while number:
        bytes_.append((number & mask) | msb_mask)
        number >>= 7
    bytes_[0] ^= msb_mask
    return bytes_[::-1]

def encode(numbers: list[int]) -> list[int]:
    """Returns the vlq encoding of a sequence of 32-bit unsigned integers."""
    
    encoded = []
    for number in numbers:
        encoded.extend(encode_integer(number))
    return encoded

def decode_integer(bytes_: list[int]) -> int:
    """Returns the decoded integer corresponding to a vlq sequence of bytes

    Parameters
    ----------
    bytes_:
        A sequence of vlq encoding bytes.

    Returns
    -------
    The integer corresponding to the decoded input.

    Raises
    ------
    ValueError
        If the sequence of bytes isn't valid.
    """
        
    mask = 0b1111111
    bytes_ = reversed(bytes_)
    
    result = sum(
        (byte & mask) * 2**(7 * i)
        for i, byte in enumerate(bytes_)
    )

    # max_unsigned_int32 = 2**32 - 1 = 4294967295
    if result > 4294967295:
        raise ValueError("Invalid sequence")

    return result

def decode(bytes_: list[int]) -> list[int]:
    """Returns the decoded integer sequence corresponding to a vlq sequence of bytes"""

    if not bytes_:
        return []

    msb_mask = 0b10000000
    if bytes_[-1] & msb_mask:
        raise ValueError("incomplete sequence")

    integers = []
    integer = []
    for byte in bytes_:
        integer.append(byte)
        if byte & msb_mask == 0:
            integers.append(integer)
            integer = []
    
    return [decode_integer(integer) for integer in integers]
    