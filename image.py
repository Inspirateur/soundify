#!/usr/bin/env python3
"""
internal image class
"""

from PIL import Image as pil
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
        self._raw = np.reshape(np.array(image.getdata(), dtype=np.uint8), (self.size + (-1,)))
        print(self._raw)
        print(np.shape(self._raw))
        if sweeping_func is not None:
            self._generate_data()
            pass
        else:
            self.data = self._raw


    def _generate_data(self):
        data = np.zeros((np.prod(self.size), 3))
        for i, point in enumerate(self.sweep(self.size)):
            data[i] = self._raw[point]
        self.data = data

    def _generate_raw(self):
        raw = np.zeros(self.size + (3,), dtype=np.uint8)
        print(np.shape(raw))
        print(np.shape(self.data))
        for i, point in enumerate(self.sweep(self.size)):
            if i <= 1024:
                print(point)
            raw[point[0], point[1], :] = self.data[i,:]
        return raw

    def save(self, filename: str):
        raw = self._generate_raw()
        pil.fromarray(raw, mode=self.mode).save(filename)
