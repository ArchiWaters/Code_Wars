def find_next_square(sq):
    from math import sqrt
    s = sqrt(sq)
    if s == int(s):
        return (s+1)**2
    else:
        return -1


find_next_square(319225)