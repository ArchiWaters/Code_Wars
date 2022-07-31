def calculator(txt):
    for n in txt:
        if n != '.' and n != ' ':
            s = txt.index(n)
            s_val = n
    x = txt.count('.', 0, s)
    y = txt.count('.', s, len(txt))
    if '-' in txt:
        return (x - y) * '.'
    elif '+' in txt:
        return (x + y) * '.'
    elif '*' in txt:
        return (x * y) * '.'
    elif '//' in txt:
        return (x // y) * '.'
    elif x < y:
        return 0 * ''
