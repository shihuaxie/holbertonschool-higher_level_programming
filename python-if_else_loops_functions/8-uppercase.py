#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        num = ord(ch)
        if 97 <= num <= 122:
            ch = chr(num - 32)
        print("{}".format(ch), end="")  # 1st print：characters
    print()                             # 2nd print：newline
