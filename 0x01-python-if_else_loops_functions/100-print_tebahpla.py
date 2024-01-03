#!/usr/bin/python3
# 100-print_tebahpla.py
# Tony Mwangi Mugi <tonymugi074@gmail.com>

for char in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char)), end='' if char != ord('A') else '\n')
