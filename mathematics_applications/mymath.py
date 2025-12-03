import math


def r2d(rad):
    """Converts radians to degrees

    Args:
        rad (float): radians

    Returns:
        float: degrees
    """
    deg = rad * (180 / math.pi)

    return deg


def d2r(deg):
    """Converts degrees to radians

    Args:
        deg (float): degrees

    Returns:
        float: radians
    """
    rad = deg * (math.pi / 180)

    return deg