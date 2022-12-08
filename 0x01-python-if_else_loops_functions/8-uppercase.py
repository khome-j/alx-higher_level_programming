#!/usr/bin/python3

def uppercase(str):
    words = ""
    for i in str:
        if (ord(i) >= 97) and (ord(i) <= 122):
            words += chr(ord(i) - 32)
        else:
            words += i
    print(words)
