#!/usr/bin/env python3
"""
display hilbert curve
"""

from hilbert import hilbert
import turtle as ttl

#pylint:disable-all

def height(n):
    return 2 ** n - 1

def main():
    """
    main function here
    """
    n = int(input("Which iterration would you like to visualize? "))
    # origin point
    ox, oy = -300, -300
    draw = ttl.Turtle()
    draw.ht()
    draw.speed(0)
    draw.up()
    draw.goto(ox, oy)
    draw.down()
    coeff = 600 / height(n)
    for x, y in hilbert((2 ** n, 2 ** n)):
        draw.goto(ox + coeff*x, oy + coeff*y)
    ttl.mainloop()

if __name__ == "__main__":
    main()
