import string

def swap_case():
    s = "HackerRank.com presents 'Pythonist 2'."
    new_str = ""
    for i in s:
        if i.islower():
            new_str += i.capitalize()
        elif i.isupper():
            new_str += i.lower()
        else:
            new_str += i
    print(new_str)

swap_case()
