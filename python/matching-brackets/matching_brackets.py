def is_paired(input_string: str, brackets: dict | None = None) -> bool:
    """Returns if all pairs of brackets are matched and nested correctly in a string

    Parameters
    ----------
    input_string:
        The string to be checked.
    brackets: dict, optional
        The set of brackets to be verified. 
        Must be dictionary of the form: `{opening_bracket: corresponding_closing_bracket}`
        If not specified, brackets = {
            '(': ')', 
            '{': '}', 
            '[': ']', 
        }
    
    Returns
    -------
    `True` if all pairs of brackets are matched and nested correctly, otherwise `False`.
    """

    # using a list as stack
    brackets_stack = []
    if brackets is None:
        opening_brackets = {
            '(': ')', 
            '{': '}', 
            '[': ']', 
        }
    else:
        opening_brackets = brackets
    closing_brackets = set(opening_brackets.values())
    
    for char in input_string:
        if char in opening_brackets:
            brackets_stack.append(opening_brackets.get(char))
        elif char in closing_brackets:
            if not brackets_stack:
                return False
            expected = brackets_stack.pop()
            if expected != char:
                return False

    return not brackets_stack