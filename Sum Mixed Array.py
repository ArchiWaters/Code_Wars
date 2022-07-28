#Given an array of integers as strings and numbers,
#return the sum of the array values as if all were numbers.

def sum_mix(arr):
    sum = 0
    for num in arr:
        s = int(num)
        sum += s
    return sum