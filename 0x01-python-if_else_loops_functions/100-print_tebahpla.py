#!/usr/bin/python3
# 100-print_tebahpla.py
# Tony Mwangi Mugi <tonymugi074@gmail.com>

for char in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char)), end='' if char % 2 == 0 else chr(char - 32))
