import numpy as np


def Binomial_Price_Tree(CurrentPrice, Uptick, NumberOfPeriods):
    Price = np.array([CurrentPrice])
    yield Price
    for i in range(NumberOfPeriods):
        Price = np.r_[Price * Uptick, Price[-1] / Uptick]
        yield Price


def European_Option_Pricing(Payoff, DiscountFactor, RiskNeutralProb):
    Premium = Payoff[-1]
    yield Premium
    for i in range(len(Payoff) - 1):
        Premium = (RiskNeutralProb * Premium[:-1] +
                   (1.0 - RiskNeutralProb) * Premium[1:]) * DiscountFactor
        yield Premium


def American_Option_Pricing(Payoff, DiscountFactor, RiskNeutralProb):
    Premium = Payoff[-1]
    yield Premium
    for i in range(2, len(Payoff) + 1):
        Premium = np.maximum(Payoff[-i],
                             (RiskNeutralProb * Premium[:-1]
                              + (1.0 - RiskNeutralProb) * Premium[1:])
                             * DiscountFactor)
        yield Premium


S = 100.0
K = 100.0
u = 1.05
d = 1.0/u
f = 1.02
N = 3
q = (f - d) / (u - d)
Price = [S for S in Binomial_Price_Tree(S, u, N)]
Payoff_Call = [np.maximum(S - K, 0.0) for S in Price]
European_Call = [C for C in European_Option_Pricing(Payoff_Call, 1.0/f, q)]
Payoff_Put = [np.maximum(K - S, 0.0) for S in Price]
European_Put = [P for P in European_Option_Pricing(Payoff_Put, 1.0/f, q)]
American_Put = [P for P in American_Option_Pricing(Payoff_Put, 1.0/f, q)]
