#!/usr/bin/env python3
"""
display hilbert curve
"""

import time
import turtle as ttl

from vhilbert import hilbert as vhilbert
from hilbert import hilbert

#pylint:disable-all

def height(n):
    return 2 ** n - 1

def profile():
    max_iter = 12
    print("[profiling hilbert] ...", end=" ")
    t = time.time()
    for n in range(max_iter):
        for x, y in hilbert((2**n, 2**n)):
            pass
    final = round(time.time() - t, 3)
    print(f"Done ! time={final}s")
    print("[profiling vhilbert] ...", end=" ")
    t2 = time.time()
    for n in range(max_iter):
        for x, y in vhilbert((2**n, 2**n)):
            pass
    final = round(time.time() - t2, 3)
    print(f"Done ! time={final}s")

def main():
    """
    main function here
    """
    n = int(input("Which iterration would you like to visualize? "))
    if n >= 0:
        # origin point
        ox, oy = -300, -300
        draw = ttl.Turtle()
        draw.ht()
        draw.speed(0)
        draw.up()
        draw.goto(ox, oy)
        draw.down()
        coeff = 600 / height(n)
        for x, y in vhilbert((2 ** n, 2 ** n)):
            draw.goto(ox + coeff*x, oy + coeff*y)
        ttl.mainloop()
    else :
        profile()

if __name__ == "__main__":
    main()
