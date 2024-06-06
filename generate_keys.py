from sympy import randprime
from math import gcd

def keys_generator():
    p, q = randprime(100, 999), randprime(100, 999)
    n = p*q
    fn = (p-1)*(q-1)
    e = 0
    for i in range(2, fn):
        if gcd(i, fn) == 1:
            e = i 
            break
    d = pow(e, -1, fn)
    return [(n, e), (n, d)]
           
