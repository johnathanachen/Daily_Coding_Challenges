s = "AASDSDDSa"

def any_alnum(s):
    for i in s:
        while len(s) != 0:
            if i.isalnum():
                return True
            else:
                s = s[1:] + s[:2]
                any_digit(s)
        return False


def any_alpha(s):
    for i in s:
        while len(s) != 0:
            if i.isalpha():
                return True
            else:
                s = s[1:] + s[:2]
                any_digit(s)
        return False

def any_digit(s):
    for i in s:
        while len(s) != 0:
            if i.isdigit():
                return True
            else:
                s = s[1:] + s[:2]
                any_digit(s)
        return False

def any_lower(s):
    for i in s:
        while len(s) != 0:
            if i.islower():
                return True
            else:
                s = s[1:] + s[:2]
                any_digit(s)
        return False

def any_upper(s):
    for i in s:
        while len(s) != 0:
            if i.isuuper():
                return True
            else:
                s = s[1:] + s[:2]
                any_digit(s)
        return False



def print_all():
    alnum = any_alnum(s)
    alpha = any_alpha(s)
    digit = any_digit(s)
    lower = any_lower(s)
    upper = any_upper(s)
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

print_all()
