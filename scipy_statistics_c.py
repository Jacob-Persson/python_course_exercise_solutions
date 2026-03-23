# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:24:20 2026

@author: jacpe396
"""

# c. Test if two sets of (independent) random data comes from the same 
# distribution
# Hint: Have a look at the ttest_ind function

import numpy as np
from scipy import stats

# 1. Create two independent sets of data
# Set A and B from the same distribution
data_a = stats.norm.rvs(loc=10, scale=2, size=100)
data_b = stats.norm.rvs(loc=10, scale=2, size=100)

# Set C from a different distribution (different mean)
data_c = stats.norm.rvs(loc=12, scale=2, size=100)

# 2. Perform the T-test
t_stat_ab, p_val_ab = stats.ttest_ind(data_a, data_b)
t_stat_ac, p_val_ac = stats.ttest_ind(data_a, data_c)

# 3. Print and interpret results
print(f"Comparison A vs B: p-value = {p_val_ab:.4f}")
if p_val_ab < 0.05:
    print("Result: Likely from DIFFERENT distributions (reject null).")
else:
    print("Result: Likely from SAME distribution (fail to reject null).")

print(f"\nComparison A vs C: p-value = {p_val_ac:.4f}")
if p_val_ac < 0.05:
    print("Result: Likely from DIFFERENT distributions (reject null).")
else:
    print("Result: Likely from SAME distribution (fail to reject null).")