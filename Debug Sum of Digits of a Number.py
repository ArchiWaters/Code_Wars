def get_sum_of_digits(num):
    sum = 0
    num = str(num)
    for x in num:
        sum += int(x)
    return sum

