def area(a, h):
    """
    This function eval area of triangle
        Parameters:
            a: side length of triangle
            h: height to side length of triangle
        Return:
            area: area of triangle
        Example:
            area(2, 4): 4
    """
    if str(a).isdigit() and str(h).isdigit() and int(a) > 0 and int(h) > 0:
        return int(a) * int(h) / 2
    else:
        return 0


def perimeter(a, b, c):
    """
    This function eval perimeter of triangle
        Parameters:
            a: side length of triangle
            b: side length of triangle
            c: side length of triangle
        Return:
            perimeter: perimeter of triangle
        Example:
            perimeter(1, 2, 3): 6
    """
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit() and int(a) > 0 and int(b) > 0 and int(c) > 0:
        return int(a) + int(b) + int(c)
    else:
        return 0
