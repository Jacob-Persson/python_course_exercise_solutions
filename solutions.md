Solutions day3

3a. I would rewrite the script from scratch, using built in numpy matrix multiplication instead of nested loops.



3b. Line 52 followed by lines 26, 25 and 29.



3c. 0.07 s/run (compared to 1.83 s/run).



5\. I don't have an nvidia card on my uu laptop so I couldn't run cupy, but I installed dpnp instead (Intels equivalent). I tried sizes up to 2^15x2^15 but numpy outperformed dpnp at all sizes even with float32 (though the relative difference was smaller at larges sizes). It took about 30 seconds at 2^15x2^15 so I didn't try 2^16x2^16.





Exercise

3\. Profiling

In this section, you should get more familiar with code profiling, in particular with the tools cProfile, line\_profiler and scalene. Have a look at slides from this morning's session to understand what they are doing and when you should use them. Try out profiling both from the command line and using interactive python (e.g. jupyter notebook). If you get Command not found when running kernprof try searching for it in \~/.local/bin/kernprof. Alternatively install it using Anaconda/conda (e.g. conda install line\_profiler).



a. Investigate the performance of the matmult.py script

In which line(s) of the script would you start optimizing for speed?



b. Investigate the performance of the euler72.py script

In which line(s) of the script would you start optimizing for speed? (This is one problem from the euler project: https://projecteuler.net/problem=72)



c. Improve the performance of the matmult.py script

What is the best performance that you achieved with N=250?



5\. GPU Computing

In this exercise we'll test the speed advantage of CuPy over NumPy in different circunstances. We'll use Google Colab as a way to run GPU code. Go to https://colab.research.google.com and create a new notebook. By default notebooks don't have GPU capabilities. To turn on the GPU go to Edit -> Notebook settings -> Hardware accelerator -> GPU



You can now run !nvidia-smi and should be able to see something like:



Tue Mar  7 12:19:49 2023       

+-----------------------------------------------------------------------------+

| NVIDIA-SMI 525.85.12    Driver Version: 525.85.12    CUDA Version: 12.0     |

|-------------------------------+----------------------+----------------------+

| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |

| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |

|                               |                      |               MIG M. |

|===============================+======================+======================|

|   0  Tesla T4            Off  | 00000000:00:04.0 Off |                    0 |

| N/A   49C    P0    25W /  70W |      0MiB / 15360MiB |      0%      Default |

|                               |                      |                  N/A |

+-------------------------------+----------------------+----------------------+

&#x20;                                                                              

+-----------------------------------------------------------------------------+

| Processes:                                                                  |

|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |

|        ID   ID                                                   Usage      |

|=============================================================================|

|  No running processes found                                                 |

+-----------------------------------------------------------------------------+

in this case showing a Tesla T4 GPU available, although in your case the hardware might be different.



You can now import cupy and numpy to compare them. Use %timeit to compare the time to do a 2D Fourier transform on arrays of size 128x128, 256x256, 512x512, 1024x1024 and 2048x2048, between numpy and cupy. At what sizes does cupy outperform? What happens now if you set the datatype of the array to numpy.float32?

