#!/usr/bin/python3
import string

for i in string.ascii_lowercase:
    if (i == "q" or i == "e"):
        continue
    print("{}".format(i), end="")
