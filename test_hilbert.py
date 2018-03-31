#!/usr/bin/env python3
"""
display hilbert curve
"""

from hilbert import hilbert
import turtle as ttl

#pylint:disable-all

def height(n):
    if n == 1:
        return 1
    return 2*height(n-1) + 1

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
    for x, y in hilbert(n):
        draw.goto(ox + coeff*x, oy + coeff*y)
    ttl.mainloop()

if __name__ == "__main__":
    main()
