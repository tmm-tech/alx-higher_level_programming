#!/usr/bin/python3
# 2-print_alphabet.main_0.py
# Tony Mwangi Mugi <tonymugi074@gmail.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
