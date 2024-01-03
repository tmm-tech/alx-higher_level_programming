#!/usr/bin/python3
# 100-print_tebahpla.py
# Tony Mwangi Mugi <tonymugi074@gmail.com>


for char in reversed(range(ord('A'), ord('Z')+1)):
    print(f"{chr(char)}{chr(char + 32)}", end='')
