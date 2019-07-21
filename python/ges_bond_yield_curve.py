import numpy as np
import numpy.polynomial.polynomial as pol
import numpy.linalg as la
import matplotlib.pyplot as plt


def Bond_Yield(Price, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((-Price, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon))
    Roots = pol.polyroots(CF)
    Real = np.real(Roots[np.isreal(Roots)])
    Positive = (Real[Real > 0.0]).item(0)
    return (1.0 / Positive - 1.0) * 100


Bond = np.array([
    [ 99.90,  1, 2.0],
    [100.10,  2, 2.3],
    [100.66,  3, 2.6],
    [ 99.77,  4, 2.4],
    [ 98.38,  5, 2.2],
    [ 96.00,  6, 1.9],
    [ 93.70,  7, 1.7],
    [ 95.32,  8, 2.1],
    [ 95.21,  9, 2.2],
    [ 97.00, 10, 2.5]
])
F = 100
Yield = np.array([Bond_Yield(Bond[idx,0], Bond[idx,1], Bond[idx,2], F)
                  for idx in range(0, Bond.shape[0])])
P = Bond[:,0]
C = F * np.identity(Bond.shape[0]) \
    + np.tril(np.transpose(np.tile(0.01 * Bond[:, 2] * F, (Bond.shape[0], 1))))
V = la.solve(C, P)
ZeroRate = (np.power(1.0 / V, 1.0 / Bond[:, 1]) - 1.0) * 100
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(Bond[:,1], ZeroRate, 'b-')
plt.plot(Bond[:,1], Yield, 'r--')
plt.xlabel('time to maturity')
plt.ylabel('yield')
plt.legend(['yield curve (zero-coupon bond)',
            'yield curve (coupon-bearing bond)'], loc='best', frameon=False)
plt.show()
