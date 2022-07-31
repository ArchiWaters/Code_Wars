def xo(s):
    s = s.lower()
    k_x = 0; k_o = 0
    for num in s:
        if num == 'x':
            k_x += 1
        elif num == 'o':
            k_o += 1
    if k_x == k_o or k_x == k_o == 0:
        return True
    else:
        return False


#очень элегентное решение
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')