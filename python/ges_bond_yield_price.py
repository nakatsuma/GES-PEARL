import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt


def Bond_Yield(Price, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((-Price, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon))
    Roots = pol.polyroots(CF)
    Real = np.real(Roots[np.isreal(Roots)])
    Positive = (Real[Real > 0.0]).item(0)
    return (1.0 / Positive - 1.0) * 100


def Bond_Price(Yield, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((0.0, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon))
    return pol.polyval(1.0 / (1.0 + 0.01 * Yield), CF)


P_A = Bond_Price(7, 7, 5, 100)
Y_B = Bond_Yield(98, 5, 5, 100)
V_Yield = np.linspace(0, 12, 41)
V_Price = np.array([Bond_Price(Yield, 7, 5, 100) for Yield in V_Yield])
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(V_Yield, V_Price, 'b-')
plt.xlabel('yield')
plt.ylabel('price')
plt.show()
