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
    length = 15
    colors = np.array([1/length * np.array((i, j, k))
                       for i in range(length + 1)
                       for j in range(length + 1)
                       for k in range(length + 1)])

    numbers = color2number(colors)
    plt.figure()
    plt.plot(np.real(numbers), np.imag(numbers), 'r+')
    colors = number2color(numbers)
    print(colors)

    plt.show()


if __name__ == "__main__":
    main()
