#!/usr/bin/env python3

import numpy as np

ROT = np.array([[0, -1],
                [1, 0]])

SYM = np.array([[0, 1],
                [1, 0]])

REFL = np.array([[1, 0],
                 [0, -1]])

UP = np.array([[0],
               [1]])

RIGHT = np.array([[1],
                  [0]])

DOWN = -1*UP

#Memoized dict 
HILBERT = {}

def _hilbert(n):
    if n in HILBERT:
        return HILBERT[n]
    if n == 0:
        zero = np.zeros((2,1))
        HILBERT[0] = zero
        return zero

    v = _hilbert(n-1)

    v1 = np.matmul(SYM, v)

    v2 = (v1[:,-1:] + UP) + v

    v3 = (v2[:,-1:] + RIGHT) + v

    v4 = (v3[:,-1:] + DOWN) + np.matmul(REFL ,np.matmul(ROT, v))

    vf = np.concatenate((v1, v2, v3, v4), axis=1)
    HILBERT[n] = vf
    return vf

def hilbert(size):
    w, h = size
    assert w == h
    assert not (w & (w - 1))
    n = int(np.log2(w))
    mat = _hilbert(n).T
    return mat