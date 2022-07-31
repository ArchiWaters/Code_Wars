def vaporcode(s):
    s = s.upper()
    for char in s:
        if char != ' ':
            print(char + ' ', end='')

vaporcode("Why isn't my code working?")