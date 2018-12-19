import numpy as np
import scipy.linalg as la
import pandas as pd
stockvalue = pd.read_csv('capm.csv', index_col=0)
R = (stockvalue.diff()/stockvalue.shift(1))[1:] * 100
R.index = pd.date_range('2013-4-1', periods=R.shape[0], freq='M')
Y = R['TOPIX']
del R['TOPIX']
T = R.shape[0]
StockList = R.columns
Coefs = pd.DataFrame([la.lstsq(np.vstack((np.ones(T), Y)).T, R[Stock])[0] \
                     for Stock in StockList],
                     index=StockList, columns=['Alpha','Beta'])
