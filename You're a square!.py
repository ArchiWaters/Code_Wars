def is_square(n):
    from math import sqrt
    if n < 0:
        return False
    elif n == 0:
        return True
    elif sqrt(n).is_integer():
        return True
    else:
        return False
