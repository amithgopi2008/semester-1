class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.

        Raises:
            TypeError: if pounds or pence is not an integer.
            ValueError: if pounds is negative, or pence is outside 0–99.
        """
        # Type checks (TypeError takes priority over ValueError)
        if not isinstance(pounds, int) or isinstance(pounds, bool):
            raise TypeError(f"pounds must be an int, got {type(pounds).__name__}")
        if not isinstance(pence, int) or isinstance(pence, bool):
            raise TypeError(f"pence must be an int, got {type(pence).__name__}")

        # Range checks
        if pounds < 0:
            raise ValueError(f"pounds must be >= 0, got {pounds}")
        if not (0 <= pence <= 99):
            raise ValueError(f"pence must be between 0 and 99, got {pence}")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money, e.g. '£1.05'.
        Pence is zero-padded to two digits.
        """
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total as a new Money.

        Raises:
            TypeError: if other is not a Money object.
        """
        if not isinstance(other, Money):
            raise TypeError(f"can only add Money to Money, not {type(other).__name__}")

        total_pence = self.pence + other.pence
        carry = total_pence // 100
        new_pence = total_pence % 100
        new_pounds = self.pounds + other.pounds + carry

        return Money(new_pounds, new_pence)