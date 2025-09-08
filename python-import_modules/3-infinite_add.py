#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0
    for i in args:
        total = total + int(i)
    print(total)
