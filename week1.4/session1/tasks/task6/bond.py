def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    target = [0, 0, 7]
    matched = 0

    for num in intList:
        if num == target[matched]:
            matched += 1
            if matched == 3:
                return True

    return False