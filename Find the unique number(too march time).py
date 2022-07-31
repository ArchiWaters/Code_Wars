def find_uniq(arr):
    max_val = max(arr); min_val = min(arr); k = 0
    for num in arr:
        if num == min_val:
            k += 1
    if k > 1:
        print(max_val)
        return max_val
    else:
        print(min_val)
        return  min_val


find_uniq([ 3, 2, 3, 3, 3 ])