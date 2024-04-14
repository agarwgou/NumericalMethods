import math
import numpy as np
from .binomial import EuropeanOption, PayoffType, bsPrice,AmericanOption

def lsmcAmerican(S0, r, q, vol, nPaths, nT, trade):

    T = trade.expiry
    K = trade.strike
    payoff = trade.payoffType

    I = nPaths
    M = nT
    dt=T/M
    df=math.exp(-r*dt)
    sigma = vol

    delta_X = (r - sigma*sigma/2)*dt + (sigma * np.sqrt(dt)* np.random.standard_normal((I,M)))
    delta_X = np.hstack((np.reshape(np.zeros(I),(-1,1)), delta_X))
    S=S0*np.exp(np.cumsum(delta_X, axis=1))

    h = trade.payoff(S)
    V= h.T[-1]
    for i in range(M-1,0,-1):
        rg = np.polyfit(S.T[i],V*df,5)
        C = np.polyval(rg,S.T[i])
        V=np.where(h.T[i]>C,h.T[i],V*df)

    V0 = df * np.average(V)

    return V0