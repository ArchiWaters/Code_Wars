def min_max(lst):
    my_lst = []
    min_lst = min(lst)
    my_lst.append(min_lst)
    max_lst = max(lst)
    my_lst.append(max_lst)
    my_lst.sort()
    return my_lst

def min_max(lst):
    return [min(lst), max(lst)]