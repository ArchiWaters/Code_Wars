def expression_matter(a, b, c):
    my_list = []
    a1 = a * (b + c)
    my_list.append(a1)
    a2 = a * b * c
    my_list.append(a2)
    a3 = a + b * c
    my_list.append(a3)
    a4 = (a + b) * c
    my_list.append(a4)
    return max(my_list)


expression_matter(3, 3, 3)