import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt


def Bond_Price(Yield, Maturity, CouponRate, FaceValue):
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((0.0, np.tile(Coupon, int(Maturity) - 1), FaceValue + Coupon))
    return pol.polyval(1.0 / (1.0 + 0.01 * Yield), CF)


def Bond_Duration(Yield, Maturity, CouponRate, FaceValue):
    Price = Bond_Price(Yield, Maturity, CouponRate, FaceValue)
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((np.tile(Coupon, int(Maturity) - 1), Coupon + FaceValue))
    Coef = np.linspace(1, Maturity, Maturity) * CF
    return pol.polyval(1.0 / (1.0 + 0.01 * Yield), np.hstack((0.0, Coef))) / Price


def Bond_Convexity(Yield, Maturity, CouponRate, FaceValue):
    Price = Bond_Price(Yield, Maturity, CouponRate, FaceValue)
    Duration = Bond_Duration(Yield, Maturity, CouponRate, FaceValue)
    Coupon = 0.01 * CouponRate * FaceValue
    CF = np.hstack((np.tile(Coupon, int(Maturity) - 1), Coupon + FaceValue))
    Coef = (np.linspace(1, Maturity, Maturity) - Duration)**2 * CF
    Dispersion = pol.polyval(1.0 / (1.0 + 0.01 * Yield), np.hstack((0.0, Coef))) \
                 / Price
    return (Dispersion + (1.0 + Duration) * Duration) / (1.0 + 0.01 * Yield)**2


P_A = Bond_Price(5, 10, 7, 100)
P_B = Bond_Price(5, 8, 0.9, 100)
D_A = Bond_Duration(5, 10, 7, 100)
D_B = Bond_Duration(5, 8, 0.9, 100)
C_A = Bond_Convexity(5, 10, 7, 100)
C_B = Bond_Convexity(5, 8, 0.9, 100)
V_Yield = np.linspace(0, 12, 41)
V_Price_A = np.array([Bond_Price(Yield, 10, 7, 100) for Yield in V_Yield])
V_Price_B = np.array([Bond_Price(Yield, 8, 0.9, 100) for Yield in V_Yield])
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(V_Yield, V_Price_A / P_A, 'b-')
plt.plot(V_Yield, V_Price_B / P_B, 'r--')
plt.axhline(1, color='k', linestyle=':', linewidth=0.5)
plt.axvline(5, ymin=0, ymax=0.8, color='k', linestyle=':', linewidth=0.5)
plt.xlabel('yield')
plt.ylabel('price')
Legend_A = 'bond A (D ={0:8.4f}, C ={1:8.4f})'.format(D_A, C_A)
Legend_B = 'bond B (D ={0:8.4f}, C ={1:8.4f})'.format(D_B, C_B)
plt.legend([Legend_A, Legend_B], loc='best', frameon=False)
plt.show()
