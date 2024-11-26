def area(a, b):
    """
    This function eval area of rectangle
        Parameters:
            a: side length of rectangle
            b: side length of rectangle
        Return:
            area: area of rectangle
        Example:
            area(2, 4): 8
    """
    if str(a).isdigit() and str(b).isdigit() and int(a) > 0 and int(b) > 0:
        return int(a) * int(b)
    else:
        return 0


def perimeter(a, b):
    """
    This function eval perimeter of rectangle
        Parameters:
            a: side length of rectangle
            b: side length of rectangle
        Return:
            perimeter: perimeter of rectangle
        Example:
            perimeter(2, 4): 12
    """
    if str(a).isdigit() and str(b).isdigit() and int(a) > 0 and int(b) > 0:
        return (int(a) + int(b)) * 2
    else:
        return 0
