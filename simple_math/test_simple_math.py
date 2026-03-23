# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:13:46 2026

@author: jacpe396
"""

from simple_math import *

def test_simple_add():
    assert simple_add(1,3) == 4
    assert simple_add(5,0) == 5

def test_simple_sub():
    assert simple_sub(7,9) == -2

def test_simple_mult():
    assert simple_mult(3,4) == 12

def test_simple_div():
    assert simple_div(6,3) == 2

def test_poly_first():
    assert poly_first(2, 3, 4) == 11

def test_poly_second():
    assert poly_second(2, 3, 4, 3) == 23    