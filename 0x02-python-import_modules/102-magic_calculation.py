#!/usr/bin/python3
from calculator_1 import add,sub;
def magic_calculation(a, b):

    if a < b:
        sum = add(a, b)
        for i in range(4, 6):
            sum = add(sum, i)
        return sum
    else:
        return sub(a, b)
