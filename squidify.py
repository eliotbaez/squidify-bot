#!/usr/bin/python3
import re
import sys


protected_words = {}

def squidify_word(s):
    if s in protected_words:
        return s
    else:
        squidified = re.sub(r"(?i)^[bcdfghjklmnpqrstvwxyz]+", "squ", s)
        return squidified


def squidify(file):
    for line in file:
        for word in line.split():
            print(squidify_word(word), end=' ')
        print()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            squidify(f)
    else: 
        squidify(sys.stdin)
