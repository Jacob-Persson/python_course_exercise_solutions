# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:14:30 2026

@author: jacpe396
"""

#a. Create a discrete random variable with poissonian distribution and plot 
#its probability mass function (PMF), cummulative distribution function (CDF) 
#and a histogram of 1000 random realizations of the variable

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# 1. Setup
mu = 4.0
x = np.arange(0, 15)
pmf_values = poisson.pmf(x, mu)
cdf_values = poisson.cdf(x, mu)
random_samples = poisson.rvs(mu, size=1000)

# 2. Create the figure and the 'ax' array of subplots
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# --- Use ax[0], ax[1], and ax[2] to access the specific plots ---

# 1. Theoretical PMF (Bar Chart)
ax[0].bar(x, pmf_values, color='skyblue', edgecolor='navy', alpha=0.7)
ax[0].set_title('Poisson PMF (Theoretical)')

# 2. Cumulative Distribution Function (CDF)
ax[1].step(x, cdf_values, where='post', color='red')
ax[1].set_title('Poisson CDF')

# 3. Histogram of 1000 Random Samples
ax[2].hist(random_samples, bins=np.arange(16)-0.5, density=True, 
           color='orange', edgecolor='black', alpha=0.7)
ax[2].set_title('1000 Random Realizations')

plt.tight_layout()
plt.show()