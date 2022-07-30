#The first century spans from the year 1 up to and including the year 100,
#the second century - from the year 101 up to and including the year 200, etc.

def century(year):
    """

    :type year: object
    """
    if 1 <= year <= 100:
        return 1
    elif year % 100 == 0:
        return year // 100
    elif 101 <= year and year % 100 != 0:
        return year // 100 + 1