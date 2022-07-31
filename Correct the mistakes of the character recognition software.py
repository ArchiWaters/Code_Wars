def correct(s):
    s = s.upper()
    for n in s:
        if n == '5':
            s = s.replace('5', 'S')
        elif n == '0':
            s = s.replace('0', 'O')
        elif n == '1':
            s = s.replace('1', 'I')
    return s
correct('51NGAP0RE')

def correct(string):                                        #second variant
    return string.translate(str.maketrans("501", "SOI"))

def correct(string):                                        #third variant
    return string.replace('1','I').replace('0','O').replace('5','S')