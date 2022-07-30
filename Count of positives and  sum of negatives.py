# Given an array of integers. Return an array,
# where the first element is the count of positives
# numbers and the second element is sum of negative numbers.
# 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(arr):
    val = []; k_pos = 0; sum_neg = 0;
    if len(arr) > 0:
        for num in arr:
            if num > 0:
                k_pos += 1
            elif num < 0:
                sum_neg += num
        val.append(k_pos);
        val.append(sum_neg)
    return val
