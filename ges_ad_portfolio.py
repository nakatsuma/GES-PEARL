import numpy as np
import cvxpy as cvx
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
T, N = R.shape
Mu = R.mean().values
Return_Dev = (R - Mu).values / T
Weight = cvx.Variable(N)
Deviation = cvx.Variable(T)
Target_Return = cvx.Parameter(sign='positive')
Risk_AD = cvx.norm(Deviation, 1)
Opt_Portfolio = cvx.Problem(cvx.Minimize(Risk_AD),
                            [Return_Dev * Weight == Deviation,
                             Weight.T * Mu == Target_Return,
                             cvx.sum_entries(Weight) == 1.0,
                             Weight >= 0.0])
V_Target = np.linspace(Mu.min(), Mu.max(), num=250)
V_Risk = np.zeros(V_Target.shape)
for idx, Target_Return.value in enumerate(V_Target):
    Opt_Portfolio.solve()
    V_Risk[idx] = Risk_AD.value
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(V_Risk, V_Target, 'b-')
plt.plot((R - Mu).abs().mean().values, Mu, 'rx')
plt.legend(['frontier', 'asset'], loc='best', frameon=False)
plt.xlabel('absolute deviation (%)')
plt.ylabel('expected return (%)')
plt.show()
