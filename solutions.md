Solutions

3a. I would rewrite the script from scratch, using built in numpy matrix multiplication instead of nested loops.



3b. Line 52 followed by lines 26, 25 and 29.



3c. 0.07 s/run (compared to 1.83 s/run).





Exercise

3\. Profiling

In this section, you should get more familiar with code profiling, in particular with the tools cProfile, line\_profiler and scalene. Have a look at slides from this morning's session to understand what they are doing and when you should use them. Try out profiling both from the command line and using interactive python (e.g. jupyter notebook). If you get Command not found when running kernprof try searching for it in \~/.local/bin/kernprof. Alternatively install it using Anaconda/conda (e.g. conda install line\_profiler).



a. Investigate the performance of the matmult.py script

In which line(s) of the script would you start optimizing for speed?



b. Investigate the performance of the euler72.py script

In which line(s) of the script would you start optimizing for speed? (This is one problem from the euler project: https://projecteuler.net/problem=72)



c. Improve the performance of the matmult.py script

What is the best performance that you achieved with N=250?





