#!/usr/bin/env python3
"""
Test on numpy's fft
"""

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

def dispay_sound(sound):
    """
    display the sound
    """
    nbsamples = len(sound)
    # sampling frequency
    frate = 44100.
    # time and frequency array
    time = np.linspace(0., nbsamples / frate, nbsamples)
    # freq = rfftfreq(nbsamples, 1 / frate)
    plt.plot(time, sound)
    plt.show()


def main():
    """
    main test
    """
    nbsamples = 10000
    frate = 44100.
    time = np.linspace(0., nbsamples / frate, nbsamples)
    sound = 0.5 * np.sin(220. * 2.*np.pi * time) + 0.5*np.sin(440. * 2.0*np.pi * time)

    spectrum = fft.rfft(sound)
    freq = fft.rfftfreq(len(sound), 1 / frate)

    plt.figure(0)
    plt.plot(time, sound)
    plt.figure(1)
    plt.semilogx(freq, 2 / nbsamples * np.abs(spectrum))

    sound = fft.irfft(spectrum)

    plt.figure(3)
    plt.plot(time, sound)


    plt.show()


if __name__ == "__main__":
    main()
