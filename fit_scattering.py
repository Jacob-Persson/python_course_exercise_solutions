# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:23:16 2026

@author: jacpe396
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# 1. Load data
data_exp = np.load('I_q_IPA_exp.npy')
data_mod = np.load('I_q_IPA_model.npy')

q_exp, i_exp = data_exp[:, 0], data_exp[:, 1]
q_mod, i_mod = data_mod[:, 0], data_mod[:, 1]

# 2. Filter q_exp to stay WITHIN the bounds of q_mod
# This prevents interpolation errors/NaNs
mask = (q_exp >= q_mod.min()) & (q_exp <= q_mod.max())
q_exp_filtered = q_exp[mask]
i_exp_filtered = i_exp[mask]

# 3. Create interpolation
model_interp = interp1d(q_mod, i_mod, kind='cubic')

# 4. Updated Objective function
def objective(s):
    i_model_at_exp_q = model_interp(q_exp_filtered)
    # Use np.nansum to be extra safe against any hidden NaNs
    return np.nansum((i_exp_filtered - s * i_model_at_exp_q)**2)

# 5. Minimize
result = minimize_scalar(objective)
best_s = result.x

# 6. Visualization
plt.figure(figsize=(10, 6))
plt.scatter(q_exp, i_exp, label='Experimental Data', alpha=0.6, s=10, color='black')
plt.plot(q_exp, best_s * model_interp(q_exp), label=f'Scaled Model (s={best_s:.2f})', color='red', lw=2)

plt.xlabel('Scattering Vector (q)')
plt.ylabel('Scattering Strength (I)')
plt.title('Fitting Theoretical Model to Experimental Scattering Data')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()