# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:21:49 2026

@author: jacpe396
"""

# b. Create a continious random variable with normal distribution and plot 
# its probability mass function (PMF), cummulative distribution function (CDF) 
# and a histogram of 1000 random realizations of the variable

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. Define Parameters (mean and standard deviation)
mu, sigma = 0, 1 
x = np.linspace(-5, 5, 500) # Smooth range for the curve

# 2. Calculate PDF and CDF
pdf_values = norm.pdf(x, mu, sigma)
cdf_values = norm.cdf(x, mu, sigma)

# 3. Generate 1000 random realizations
random_samples = norm.rvs(mu, sigma, size=1000)

# Create the figure with 3 subplots
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# Plot PDF (Probability Density Function)
ax[0].plot(x, pdf_values, color='blue', lw=2)
ax[0].fill_between(x, pdf_values, color='blue', alpha=0.2)
ax[0].set_title(f'Normal PDF ($\mu={mu}, \sigma={sigma}$)')
ax[0].set_ylabel('Density')

# Plot CDF (Cumulative Distribution Function)
ax[1].plot(x, cdf_values, color='red', lw=2)
ax[1].set_title('Normal CDF')
ax[1].set_ylabel('Cumulative Probability')

# Plot Histogram of 1000 Random Samples
ax[2].hist(random_samples, bins=30, density=True, color='orange', edgecolor='black', alpha=0.7)
# Optional: Overlay the theoretical PDF on the histogram for comparison
ax[2].plot(x, pdf_values, 'k--', lw=1.5)
ax[2].set_title('Histogram (1000 Samples)')

plt.tight_layout()
plt.show()