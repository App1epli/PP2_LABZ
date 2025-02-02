#Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def ppermutations(s):
    perm = permutations(s)
    for x in perm:
        print(''.join(x))

s=input()
ppermutations(s)