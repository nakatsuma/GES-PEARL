import numpy as np
import cvxpy as cvx
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
T, N = R.shape
Mu = R.mean().values
Return = R.values / T
Weight = cvx.Variable(N)
Deviation = cvx.Variable(T)
VaR = cvx.Variable()
Alpha = cvx.Parameter(nonneg=True)
Target_Return = cvx.Parameter(nonneg=True)
Risk_ES = cvx.sum(Deviation)/Alpha - VaR
Opt_Portfolio = cvx.Problem(cvx.Minimize(Risk_ES),
                            [Weight.T*Mu == Target_Return,
                             cvx.sum(Weight) == 1.0,
                             Weight >= 0.0,
                             Deviation >= 0.0,
                             Return*Weight - VaR/T + Deviation >= 0.0])
V_Alpha = np.array([0.05, 0.10, 0.25, 0.50])
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros((V_Target.shape[0], V_Alpha.shape[0]))
for idx_col, Alpha.value in enumerate(V_Alpha):
    Alpha.value = V_Alpha[idx_col]
    for idx_row, Target_Return.value in enumerate(V_Target):
        Opt_Portfolio.solve()
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
for idx, Alpha.value in enumerate(V_Alpha):
    plt.plot(V_Risk[:, idx], V_Target, color='b', linestyle=LineTypes[idx])
plt.legend(['frontier ($\\alpha$={0:4.2f})'.format(a) for a in V_Alpha],
           loc='best', frameon=False)
plt.xlabel('expected shortfall (%)')
plt.ylabel('expected return (%)')
plt.show()
