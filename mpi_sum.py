# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:17:06 2026

@author: jacpe396
"""

from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 
rank_sum = comm.reduce(rank, op=MPI.SUM, root=0)

if rank == 0:
    print(f"The sum of all ranks is: {rank_sum}")