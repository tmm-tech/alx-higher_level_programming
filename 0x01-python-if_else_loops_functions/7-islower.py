#!/usr/bin/python3
# 7-islower.main_0.py
# Tony Mwangi Mugi <tonymugi074@gmail.com>


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
