import math


def area(r):
    """
    This function eval area of circle
        Parameters:
             r: radius of circle
        Return:
            area: area of circle
        Example:
            area(2): 4pi
    """
    if str(r).isdigit() and int(r) > 0:
        return math.pi * int(r) * int(r)
    else:
        return 0


def perimeter(r):
    """
    This function eval perimeter of circle
        Parameters:
            r: radius of circle
        Return:
            perimeter: perimeter of circle
        Example:
            perimeter(2): 4pi
    """
    if str(r).isdigit() and int(r) > 0:
        return 2 * math.pi * int(r)
    else:
        return 0
