def mystery_func(string):
    """
    Counts the number of uppercase and lowercase letters in a string.

    Iterates over each character in the input and tallies how many are
    uppercase letters and how many are lowercase letters. Non-alphabetic
    characters (digits, spaces, punctuation, symbols) are ignored and
    contribute to neither count.

    Args:
        string (str): The string to analyze.

    Returns:
        tuple of int: A tuple (upper, lower) where `upper` is the count of
        uppercase letters and `lower` is the count of lowercase letters.
    """
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)