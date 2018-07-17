#!/usr/bin/env python3
"""
Test for color modules
"""

import numpy as np
import matplotlib.pyplot as plt

from colors import number_to_color, color_to_number

def main():
    """
    main function here
    """
    length = 50
    colors = np.array([1/length * np.array((i, j, k))
                       for i in range(length + 1)
                       for j in range(length + 1)
                       for k in range(length + 1)])
    print("done")
    numbers = color_to_number(colors)
    print("done")
    plt.figure()
    plt.scatter(np.real(numbers), np.imag(numbers), None, colors, '.')
    colors = number_to_color(numbers)

    plt.show()


if __name__ == "__main__":
    main()
