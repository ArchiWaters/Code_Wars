def get_sum(a,b):
    sum_a = 0
    if a == b:
        return a
    elif a > b:
        for n in range(b, a+1):
            sum_a += n
        return sum_a
    elif a < b:
        for n in range(a,b+1):
            sum_a += i
        return sum_a