#!/usr/bin/env python3
"""
Test on numpy's fft
"""

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt


def main():
    """
    main test
    """
    nbsamples = 10000
    frate = 44100.
    time = np.linspace(0., nbsamples / frate, nbsamples)
    sound = np.sin(220. * 2.*np.pi * time) + 0.5*np.sin(440. * 2.0*np.pi * time)

    spectrum = np.abs(fft.rfft(sound))
    freq = fft.rfftfreq(len(sound), 1 / frate)

    plt.figure(0)
    plt.plot(time, sound)
    plt.figure(1)
    plt.semilogx(freq, 2 / nbsamples * np.abs(spectrum))

    sound = fft.irfft(spectrum)

    plt.figure(2)
    plt.plot(time, sound)

    plt.show()


if __name__ == "__main__":
    main()
