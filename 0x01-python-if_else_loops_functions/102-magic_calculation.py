#!/usr/bin/python3
def magic_calculation(a, b, c):
    if b < a:
        return c
    elif b > c:
        return a + b
    else:
        return a * b - c
