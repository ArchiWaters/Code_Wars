#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    n = str(n); val = []
    for num in n:
        val.append(int(num))
    val.reverse()
    print(val)
    return val

digitize(35231)

#best solution
def digitize(n):
    return [int(x) for x in reversed(str(n))]