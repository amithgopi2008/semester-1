def filter_positive_numbers(numbers):
    """
    Filters out non-positive numbers from the list, keeping only the positive ones.
    The function returns a list of all the positive numbers in the input.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing only the positive integers.
    """
    return [num for num in numbers if num > 0]

