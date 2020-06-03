import numpy as np
import cvxpy as cp
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
T, N = R.shape
Mu = R.mean().values
Return = R.values / T
Weight = cp.Variable(N)
Deviation = cp.Variable(T)
VaR = cp.Variable()
inv_Alpha = cp.Parameter(nonneg=True)
Target_Return = cp.Parameter(nonneg=True)
Risk_ES = cp.sum(Deviation) * inv_Alpha - VaR
Opt_Portfolio = cp.Problem(cp.Minimize(Risk_ES),
                           [Weight.T @ Mu == Target_Return,
                            cp.sum(Weight) == 1.0,
                            Weight >= 0.0,
                            Deviation >= 0.0,
                            Return @ Weight - VaR / T + Deviation >= 0.0])
V_Alpha = np.array([0.05, 0.10, 0.25, 0.50])
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros((V_Target.shape[0], V_Alpha.shape[0]))
for idx_col, Alpha in enumerate(V_Alpha):
    inv_Alpha.value = 1.0 / Alpha
    for idx_row, Target_Return.value in enumerate(V_Target):
        Opt_Portfolio.solve(solver=cp.ECOS)
        V_Risk[idx_row, idx_col] = Risk_ES.value
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(V_Risk[:, 0], V_Target, 'b-')
plt.plot((-R[R <= R.quantile(V_Alpha[0])]).mean().values, Mu, 'rx')
plt.legend(['frontier', 'asset'], loc='best', frameon=False)
plt.xlabel('expected shortfall (%)')
plt.ylabel('expected return (%)')
plt.show()
fig2 = plt.figure(num=2, facecolor='w')
LineTypes = ['solid', 'dashed', 'dashdot', 'dotted']
for idx in range(len(V_Alpha)):
    plt.plot(V_Risk[:, idx], V_Target, color='b', linestyle=LineTypes[idx])
plt.legend(['frontier ($\\alpha$={0:4.2f})'.format(a) for a in V_Alpha],
           loc='best', frameon=False)
plt.xlabel('expected shortfall (%)')
plt.ylabel('expected return (%)')
plt.show()
