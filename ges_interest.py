import numpy as np
import matplotlib.pyplot as plt
r = 0.2
Maturity = 10
Simple_Rate = 1.0 + r * np.linspace(0, Maturity, Maturity + 1)
Compound_1year = np.hstack((1.0, np.cumprod(np.tile(1.0 + r, Maturity))))
Compound_6month = np.hstack((1.0, np.cumprod(np.tile((1.0 + r/2.0)**2, Maturity))))
Continuous_Rate = np.exp(r*np.linspace(0, Maturity, Maturity + 1))
fig1 = plt.figure(num=1, facecolor='w')
plt.plot(Simple_Rate, 'b-')
plt.plot(Compound_1year, 'r--')
plt.plot(Compound_6month, 'g-.')
plt.plot(Continuous_Rate, 'm:')
plt.legend(['simple', '1-year compound', '6-month compound', 'continuous'],
           loc='upper left', frameon=False)
plt.xlabel('t')
plt.ylabel('W(t)/W(0)')
plt.show()
