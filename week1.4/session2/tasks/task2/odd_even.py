def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """
    odd_count = 0
    even_count = 0

    for num in lstIntegers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return [odd_count, even_count]