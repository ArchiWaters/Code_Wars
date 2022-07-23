def scrabble_score(st):
    st = st.lower()
    k = 0
    for n in st:
        if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or n == 'l' or n == 'n' or n == 'r' or n == 's' or n =='t':
            k += 1
        elif n == 'd' or n == 'g':
            k += 2
        elif n == 'b' or n == 'c' or n == 'm' or n =='p':
            k += 3
        elif n == 'f' or n == 'h' or n == 'v' or n == 'w' or n == 'y':
            k += 4
        elif n == 'k':
            k += 5
        elif n == 'j' or n == 'x':
            k += 8
        elif n == 'q' or n == 'z':
            k += 10
    return k

