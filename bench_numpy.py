# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:41:59 2026

@author: jacpe396
"""

import numpy as np

# Do 2D Fourier transform of size nxn with numpy
DTYPE = np.float32
n = 2**15

data = np.random.random((n, n)).astype(DTYPE)
np.fft.fft2(data)