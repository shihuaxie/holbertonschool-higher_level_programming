#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        num = ord(ch)
        if 97 <= num <= 122:
            num = num - 32
        result = result + chr(num)
    print("{}".format(result))
