def dont_give_me_five(start,end):
    n = 0
    for nun in range(start, end+1):
        if nun%10 != 5:
            n += 1
    return n


dont_give_me_five(4,17)