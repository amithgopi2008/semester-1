class Money:
    """
    Represents an amount of money in pounds (£) and pence.
    Pence must be in the range 0–99.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object.

        Args:
            pounds (int): The number of whole pounds (must be >= 0).
            pence (int): The number of pence (0–99).

        Raises:
            TypeError: If pounds or pence is not an integer.
            ValueError: If pounds is negative or pence is outside 0–99.
        """
        # Type checks first (TypeError takes priority over ValueError)
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
        Returns a string like '£1.05' with pence zero-padded to two digits.
        """
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds two Money objects together, carrying over pence into pounds
        when the pence total exceeds 99.

        Returns:
            Money: a new Money object representing the sum.
        """
        total_pence = self.pence + other.pence
        carry = total_pence // 100          # how many whole pounds to carry
        new_pence = total_pence % 100       # leftover pence (0–99)
        new_pounds = self.pounds + other.pounds + carry

        return Money(new_pounds, new_pence)