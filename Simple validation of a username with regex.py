def validate_usr(username):
    if 4 <= len(username) <= 16:
        for n in username:
            if n == n.lower():
                if n.isdigit():
                    return True
            else:
                return False
    else:
        print('Invalid number of characters')