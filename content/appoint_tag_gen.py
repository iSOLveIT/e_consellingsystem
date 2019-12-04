# Standard library imports
import random
import string

# Local app imports


def randomDigits(stringLength=5):
    """Generate a random string of digits """
    _digits = string.digits
    # Generating a Random String including letters and digits"
    digi = ''.join(random.sample(_digits, stringLength))
    tag = digi

    return tag