from datetime import date


class Person:
    """A class representing a person."""

    def __init__(self, name, birth):
        """Initialize a Person with a name and date of birth."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if name == "":
            raise ValueError("Name cannot be empty.")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object.")

        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercase initials of the person's name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Check whether today is the person's birthday."""
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
