def find_uniq(arr):
    max_list = []; min_list = []
    for num in arr:
        if num == max(arr):
            max_list.append(num)
        elif num == min(arr):
            min_list.append(num)
    if len(max_list) == 1:
        print(max_list[0])
        return max_list[0]
    else:
        print(min_list[0])
        return min_list[0]

find_uniq([ 3, 10, 3, 3, 3 ])