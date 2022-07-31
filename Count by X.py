# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array (or list in Python, Haskell or Elixir).

def count_by(x, n):
    value_list = []
    for num in range(1, n + 1):
        value_list.append(num * x)
    return value_list