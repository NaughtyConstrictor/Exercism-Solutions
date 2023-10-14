import re

OPERATIONS = {
    "plus": int.__add__,
    "minus": int.__sub__,
    "multiplied by": int.__mul__,
    "divided by": int.__floordiv__
}

def answer(question: str) -> int:
    """Returns the result of simple math questions

    Supported operations are: addition, subtraction, multiplication and division.
    Any combination of these operations is supported.

    The function always returns an integer, so the division operation used 
    is the `floor division`.

    Examples
    --------
    `What is 5?` -> `5`
    `What is 5 plus 13?` -> `18`
    `What is 7 minus 5?` -> `2`
    `What is 6 multiplied by 4?` -> `24`
    `What is 25 divided by 5?` -> `5`
    `What is 5 plus 13 plus 6?` -> `24`

    Parameters
    ----------
    question:
        A simple math question in the form `What is ...?`.
        Check `Raises` section for more details on valid questions.
    
    Returns
    -------
    The answer after evaluating the input question.

    Raises
    ------
    ValueError:
        If the input isn't a question that starts with `What is` and ends with `?`.
        If the input isn't a math question.
        If the input contains an invalid operation.
        If the input is malformed, ex: 2 consecutive numbers not separated 
        by an operation.    
    """


    if re.search(r"-?\d+ -?\d+", question):
        raise ValueError("syntax error")
        
    match = re.search(r"^What is( -?\d+)?[\w -]*(\??)$", question)
    if match is None:
        raise ValueError("unknown operation")
    result, question_mark = match.groups()
    if not (result and question_mark):
        raise ValueError("syntax error")
    
    result = int(result)
    search_index = match.end(1)
   
    for match in re.finditer(
        r" ((?:pl|min)us|(?:multipli|divid)ed by)?([a-z]*)( -?\d+)*", 
        question[search_index:]):
        op, extra_op, operand = match.groups()
        op = OPERATIONS.get(op)
        if op is None:
            raise ValueError("unknown operation")
        if extra_op or operand is None:
            raise ValueError("syntax error")
        result = op(result, int(operand))

    return result