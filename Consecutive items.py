arr = [1, 3, 5, 7]
def consecutive(arr, a, b):
    if a and b in arr:
        if arr.index(a) == arr.index(b) - 1 or arr.index(b) == arr.index(a) - 1:
            return True
        else:
            return False

consecutive(arr,3,1)