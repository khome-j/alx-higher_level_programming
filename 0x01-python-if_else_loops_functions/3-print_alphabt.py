#!/usr/bin/python3
import string
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if (i == "q" or i == "e"):
        continue
    print(i, end="")
