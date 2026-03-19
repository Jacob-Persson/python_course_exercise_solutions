# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:00:21 2026

@author: jacpe396
"""

import dpnp as dp

# Do 2D Fourier transform of size nxn with dpnp
DTYPE = dp.float32
n = 2**15

data = dp.random.random((n, n)).astype(DTYPE)
dp.fft.fft2(data)