#!/usr/bin/python3
import string
#alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in string.ascii_lowercase:
    if (i == "q" or i == "e"):
        continue
    print("{}".format(i), end="")
