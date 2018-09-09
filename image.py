#!/usr/bin/env python3
"""
internal image class
"""

import numpy as np

class Image:
    """
    internal image class for soundify
    """
    def __init__(self, image, sweeping_func=None):

        self.size = image.size
        self.mode = image.mode
        self.format = image.format
        self.data = None

        self._raw = np.array(image.getdata())
        self.sweep = sweeping_func

        del image

    @property
    def sweep(self):
        return self._sweep
    
    @sweep.setter
    def sweep(self, value):
        if self._sweep is not None:
            raise ValueError("Sweeping function mus only be set once")
        else:
            self._sweep = value
            self._generate_data()


    def _generate_data(self):
        if self.data is not None:
            return
        self.data = np.array(self._raw[point] for point in self.sweep(self.size))
