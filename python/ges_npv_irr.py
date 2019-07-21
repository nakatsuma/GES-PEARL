import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt


def NPV(r, CF):
    x = 1.0 / (1.0 + 0.01 * r)
    return pol.polyval(x, CF)


def IRR(CF):
    Roots = pol.polyroots(CF)
    Real = np.real(Roots[np.isreal(Roots)])
    Positive = (Real[Real > 0.0]).item(0)
    return (1.0 / Positive - 1.0) * 100


Periods = np.linspace(0, 4, 5)
V_CF = np.array([[-5.0, 1.5, 1.5, 1.5, 1.5],
                 [-7.0, 2.0, 2.0, 2.0, 2.0],
                 [-9.0, 4.0, 3.0, 2.0, 1.0],
                 [-9.0, 1.0, 2.0, 3.0, 4.0]])
V_Title = ['project A', 'project B', 'project C', 'project D']
fig1 = plt.figure(num=1, facecolor='w')
for fig_num in range(4):
    plt.subplot(2, 2, fig_num + 1)
    plt.bar(Periods, V_CF[fig_num, :], color=(0.5, 0.5, 0.5))
    plt.title(V_Title[fig_num])
    plt.axhline(color='k', linewidth=0.5)
    plt.ylim(-10, 5)
    if fig_num == 2 or fig_num == 3:
        plt.xlabel('time')
    if fig_num == 0 or fig_num == 2:
        plt.ylabel('cash flow')
    if fig_num == 1 or fig_num == 0:
        plt.xticks([])
plt.show()
r = 5
V_NPV = np.zeros(4)
for cf_num in range(4):
    V_NPV[cf_num] = NPV(r, V_CF[cf_num, :])
V_IRR = np.zeros(4)
for cf_num in range(4):
    V_IRR[cf_num] = IRR(V_CF[cf_num, :])
