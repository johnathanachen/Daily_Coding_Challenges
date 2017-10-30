import textwrap

def wrap():
    s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    w = 4
    print(textwrap.fill(s,w))

wrap()
