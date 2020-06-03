import numpy as np
import cvxpy as cp
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
T, N = R.shape
Mu = R.mean().values
Return_Dev = (R - Mu).values / np.sqrt(T)
Weight = cp.Variable(N)
Deviation = cp.Variable(T)
Target_Return = cp.Parameter(nonneg=True)
Risk_Semivariance = cp.sum_squares(Deviation)
Opt_Portfolio = cp.Problem(cp.Minimize(Risk_Semivariance),
                           [Weight.T @ Mu == Target_Return,
                            cp.sum(Weight) == 1.0,
                            Weight >= 0.0,
                            Deviation >= 0.0,
                            Return_Dev @ Weight + Deviation >= 0.0])
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros(V_Target.shape)
for idx, Target_Return.value in enumerate(V_Target):
    Opt_Portfolio.solve(solver=cp.ECOS)
    V_Risk[idx] = np.sqrt(Risk_Semivariance.value)
fig1 = plt.figure(1, facecolor='w')
plt.plot(V_Risk, V_Target, 'b-')
plt.plot(np.sqrt(((R[R <= Mu] - Mu) ** 2).sum().values / T), Mu, 'rx')
plt.legend(['frontier', u'asset'], loc='best', frameon=False)
plt.xlabel('square root of semivariance (%)')
plt.ylabel('expected return (%)')
plt.show()
