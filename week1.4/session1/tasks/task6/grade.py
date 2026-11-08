def calculate_grade(marks):
    """
    This function returns a grade based on the provided mark, according to
    the following grading scale:

    Grading Rules:
    - Marks < 50: Grade is 'F'
    - Marks >= 50 and < 60: Grade is 'D'
    - Marks >= 60 and < 70: Grade is 'C'
    - Marks >= 70 and < 80: Grade is 'B'
    - Marks >= 80: Grade is 'A'

    Validity Checks:
    - Returns `None` if `marks` is not a valid positive integer between
      0 and 100 (inclusive)
    - Returns `None` if `marks` is greater than 100, as it falls outside
      the valid range

    Args:
        marks (int): A positive integer representing the student's marks.
        Valid range is 0 to 100 (inclusive)

    Returns:
        str: The grade corresponding to the marks ('A', 'B', 'C', 'D', 'F').
        None: If `marks` is not a valid integer or is outside the allowed
              range (greater than 100 or negative)
    """
    # Validity checks
    if not isinstance(marks, int) or isinstance(marks, bool):
        return None
    if marks < 0 or marks > 100:
        return None

    # Grading scale
    if marks < 50:
        grade = 'F'
    elif marks < 60:
        grade = 'D'
    elif marks < 70:
        grade = 'C'
    elif marks < 80:
        grade = 'B'
    else:
        grade = 'A'

    return grade