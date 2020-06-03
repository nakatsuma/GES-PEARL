import numpy as np
import scipy.stats as st
import cvxpy as cp
import pandas as pd
import matplotlib.pyplot as plt
R = pd.read_csv('asset_return_data.csv', index_col=0)
R = R.asfreq(pd.infer_freq(R.index))
T, N = R.shape
np.random.seed(8888)
BenchmarkIndex = R.dot(np.tile(1.0/N, N)) \
                 + st.norm.rvs(loc=0.0, scale=3.0, size=T)
MovingWindow = 96
BackTesting = T - MovingWindow
V_Tracking = np.zeros(BackTesting)
Weight = cp.Variable(N)
Error = cp.Variable(MovingWindow)
TrackingError = cp.sum_squares(Error)
Asset_srT = R / np.sqrt(T)
Index_srT = BenchmarkIndex / np.sqrt(T)
for Month in range(0, BackTesting):
    Asset = Asset_srT.values[Month:(Month + MovingWindow), :]
    Index = Index_srT.values[Month:(Month + MovingWindow)]
    Min_TrackingError = cp.Problem(cp.Minimize(TrackingError),
                                   [Index - Asset @ Weight == Error,
                                    cp.sum(Weight) == 1.0,
                                    Weight >= 0.0])
    Min_TrackingError.solve(solver=cp.ECOS)
    V_Tracking[Month] = R.values[Month + MovingWindow, :].dot(Weight.value)
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(list(range(1, BackTesting + 1)), BenchmarkIndex[MovingWindow:], 'b-')
plt.plot(list(range(1, BackTesting + 1)), V_Tracking, 'r--')
plt.legend(['benchmark index', 'index fund'], loc='best', frameon=False)
plt.xlabel('year')
plt.ylabel('return (%)')
plt.xticks(list(range(12, BackTesting + 1, 12)),
           pd.date_range(R.index[MovingWindow], periods=BackTesting//12,
                         freq='AS').year)
plt.show()
