import numpy as np
import cvxpy as cp
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
T, N = R.shape
Mu = R.mean().values
Sigma = R.cov().values * ((T - 1.0) / T)
Return_Dev = (R - Mu).values / np.sqrt(T)
Weight = cp.Variable(N)
Deviation = cp.Variable(T)
Target_Return = cp.Parameter(nonneg=True)
Risk_Variance = cp.sum_squares(Deviation)
Opt_Portfolio = cp.Problem(cp.Minimize(Risk_Variance),
                           [Return_Dev @ Weight == Deviation,
                            Weight.T @ Mu == Target_Return,
                            cp.sum(Weight) == 1.0,
                            Weight >= 0.0])
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros(V_Target.shape)
for idx, Target_Return.value in enumerate(V_Target):
    Opt_Portfolio.solve(solver=cp.ECOS)
    V_Risk[idx] = np.sqrt(Risk_Variance.value)
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(V_Risk, V_Target, 'b-')
plt.plot(np.sqrt(np.diagonal(Sigma)), Mu, 'rx')
plt.legend(['frontier', 'asset'], loc='best', frameon=False)
plt.xlabel('standard deviation (%)')
plt.ylabel('expected return (%)')
plt.show()
