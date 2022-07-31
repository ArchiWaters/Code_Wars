#1
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


#2
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e