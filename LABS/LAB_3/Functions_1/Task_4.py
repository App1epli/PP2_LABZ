#You are given list of numbers separated by spaces. Write a function filter_prime 
#which will take list of numbers as an agrument and returns only prime numbers from the list
import math

def prime(a):
    if a < 2:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    n = int(math.sqrt(a))
    for i in range(3, n+1, 2):
        if a %i==0:
            return False
    return True

def filter_prime(b):
    return [i for i in b if prime(i)]

l = list(map(int, input().split()))
print(filter_prime(l))