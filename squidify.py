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


def squidify_string(string):
    squidified_words = []
    for word in string.split():
        squidified_words.append(squidify_word(word))
    return ' '.join(squidified_words)


def squidify_file(file):
    for line in file:
        print(squidify_string(line))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            squidify_file(f)
    else: 
        squidify_file(sys.stdin)
