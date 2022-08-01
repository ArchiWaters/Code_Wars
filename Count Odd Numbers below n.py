# вернуть список нечетных числ меньше n
def odd_count(n):
    odd = []
    for s in range(n):
        if s % 2 == 1:
            odd.append(s)
    print(odd)
    return odd

odd_count(15)
