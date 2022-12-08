#!/usr/bin/python3

if __name__ == "__main__":
    import sys

args_len = len(sys.argv)
total = 0

for i in range(1, args_len):
    total += int(sys.argv[i])
print("{}".format(total))
