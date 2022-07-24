def odd_count(n):
    odd = []
    for s in range(n):
        if s % 2 == 1:
            odd.append(s)
    return odd
#вернуть список нечетных числ меньше n