def magic_calculation(a, b):
    add, sub = __import__('calculator_1', fromlist=('add', 'sub'))

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
