def area(a):
    """
    This function eval area of square
        Parameters:
            a: side length of square
        Return:
            area: area of square
        Example:
            area(3): 9
    """
    if str(a).isdigit() and int(a) > 0:
        return int(a) * int(a)
    else:
        return 0


def perimeter(a):
    """
    This function eval perimeter of square
        Parameters:
            a: side length of square
        Return:
            perimeter: perimeter of square
        Example:
            perimeter(3): 12
    """
    if str(a).isdigit() and int(a) > 0:
        return 4 * int(a)
    else:
        return 0
