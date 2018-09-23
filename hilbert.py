#!/usr/bin/env python3
"""
implementation of recursive hilbert enumeration
"""
import numpy as np

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def up(point):
    point.y += 1


def down(point):
    point.y -= 1


def left(point):
    point.x -= 1


def right(point):
    point.x += 1


def _hilbert(n, point, up=up, down=down, left=left, right=right):
    """
    recursive hilbert enumeration
    """
    if n == 0:
        yield point.x, point.y
        return
    yield from _hilbert(n - 1, point, right, left, down, up)
    up(point)
    yield from _hilbert(n - 1, point, up, down, left, right)
    right(point)
    yield from _hilbert(n - 1, point, up, down, left, right)
    down(point)
    yield from _hilbert(n - 1, point, left, right, up, down)


def hilbert(size):
    """
    API proof form of the sweeping function
    """
    w, h = size
    assert w == h
    assert not (w & (w - 1))
    n = int(np.log2(w))
    point = Point()
    yield from _hilbert(n, point)
