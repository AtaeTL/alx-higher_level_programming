#!/usr/bin/python3
"""
Prints the ASCII alphabet in lowercase.
"""

for i in range(ord('a'), ord('z')+1):
    print("{:c}".format(i), end="")
