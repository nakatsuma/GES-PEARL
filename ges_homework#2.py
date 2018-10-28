import numpy as np
import numpy.polynomial.polynomial as pol
import numpy.linalg as la
import matplotlib.pyplot as plt

def Bond_Yield(Price, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.r_[-Price, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon]
    Roots = pol.polyroots(CF)
    Real = np.real(Roots[np.isreal(Roots)])
    Positive = np.asscalar(Real[Real > 0.0])
    return (1.0 / Positive - 1.0) * 100

def Bond_Price(Yield, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.r_[0.0, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon]
    return pol.polyval(1.0 / (1.0 + 0.01 * Yield), CF)

def Bond_Duration(Yield, Maturity, CouponRate, FaceValue):
    Price = Bond_Price(Yield, Maturity, CouponRate, FaceValue)
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.r_[np.tile(Coupon, int(Maturity) - 1), Coupon + FaceValue]
    Coef = np.linspace(1, Maturity, Maturity) * CF
    return pol.polyval(1.0 / (1.0 + 0.01 * Yield), np.r_[0.0, Coef]) / Price

def Bond_Convexity(Yield, Maturity, CouponRate, FaceValue):
    Price = Bond_Price(Yield, Maturity, CouponRate, FaceValue)
    Duration = Bond_Duration(Yield, Maturity, CouponRate, FaceValue)
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.r_[np.tile(Coupon, int(Maturity) - 1), Coupon + FaceValue]
    Coef = (np.linspace(1, Maturity, Maturity) - Duration)**2 * CF
    Dispersion = pol.polyval(1.0 / (1.0 + 0.01 * Yield), np.r_[0.0, Coef]) / Price
    return (Dispersion + (1.0 + Duration) * Duration) / (1.0 + 0.01 * Yield)**2

F = 100
Bond = np.array ([
    [1, 5.00, 100.478],
    [2, 5.50, 101.412],
    [3, 6.25, 103.591],
    [4, 6.00, 103.275],
    [5, 5.75, 102.501],
    [6, 5.50, 101.199],
    [7, 4.00, 92.220],
    [8, 4.50, 94.247],
    [9, 6.50, 107.434],
    [10, 6.00, 104.213],
])
Yield = np.array([Bond_Yield(Bond[t, 2], Bond[t, 0], Bond[t, 1], F) for t in range(Bond.shape[0])])
Duration = np.array([Bond_Duration(Yield[t], Bond[t, 0], Bond[t, 1], F) for t in range(Bond.shape[0])])
Convexity = np.array([Bond_Convexity(Yield[t], Bond[t, 0], Bond[t, 1], F) for t in range(Bond.shape[0])])
P = Bond[:,2]
C = F * np.identity(Bond.shape[0]) + np.tril(np.transpose(np.tile(0.01 * Bond[:, 1] * F, (Bond.shape[0], 1))))
V = la.solve(C, P)
ZeroRate = (np.power(1.0 / V, 1.0 / Bond[:, 0]) - 1.0) * 100
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(Bond[:,0], ZeroRate, 'b-')
plt.xlabel('time to maturity')
plt.ylabel('yield')
plt.title('zero-yield curve')
plt.savefig('homework#2.png')
plt.show()
np.set_printoptions(formatter={'float': '{:7.2f}'.format})
print(np.c_[Yield, Duration, Convexity, ZeroRate])
