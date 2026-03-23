# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:10:20 2026

@author: jacpe396
"""

#mpi_ranks.py 
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 
print("hello world from process ", rank) 