#!/usr/bin/env python3
"""
Test for color modules
"""

import numpy as np
import matplotlib.pyplot as plt

from colors import number2color, color2number

def main():
    """
    main function here
    """
    length = 255
    colors = np.array([1/length * np.array((i, j, k))
                       for i in range(length + 1)
                       for j in range(length + 1)
                       for k in range(length + 1)])
    print("done")
    numbers = color2number(colors)
    print("done")
    #plt.figure()
    #plt.scatter(np.real(numbers), np.imag(numbers), None, colors, '.')
    colors = number2color(numbers)

    #plt.show()


if __name__ == "__main__":
    main()
