#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        num = ord(ch)
        if 97 <= num <= 122:
            ch = chr(num - 32)
        result = result + 1
        print("{}".format(result))
