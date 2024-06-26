# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:59:28 2024

@author: quiks
"""

# --------------------------------------------------------- Necessary Libraries  ---------------------------------------------------------
import numpy as np
import itertools
import deareis          
import pandas as pd

# --------------------------------------------------------- Edit Data Path Here ----------------------------------------------------------
data = deareis.parse_data(r'C:\Users\quiks\OneDrive\Documents\SEEDS\DATA\EX12 EX3 Redo\240410 RMB EX12-3 Psi_#5.DTA')

# --------------------------------------------------------- Create Variables -------------------------------------------------------------
v, r = '(RC)', '(C[RW])'
ECM, results, functions = ['R'], [], []

# --------------------------------------------------------- ECM Combination Generator ----------------------------------------------------
def generateComb(n,l):
        out = []
        states = np.arange(0,n,1)
        for v in itertools.combinations_with_replacement(states, l):
             out.append(v)
        return out
    
for i in range(10):
    combs = generateComb(2, i)
    for j in combs:
        baby = 'R'
        for k in j:
            if k == 0:
                baby = baby + v
            else:
                baby = baby + r
            ECM.append(baby)      
            
ecmList = list(set(ECM)) + [s + 'W' for s in list(set(ECM))]

# --------------------------------------------------------- ECM Fitter -------------------------------------------------------------------
for i in ecmList:
    settings = deareis.FitSettings(i, method = 'AUTO', weight = 'AUTO', max_nfev = 1000) 
    fit = deareis.fit_circuit(data[0], settings)
    results.append(fit.chisqr)
    functions.append(fit.method)

# --------------------------------------------------------- Best ECM Finder -------------------------------------------------------------    
results = pd.DataFrame(results)
functions = pd.DataFrame(functions)
min1, min2, min3, min4, min5 = results[0].nsmallest(5).index[0], results[0].nsmallest(5).index[1], results[0].nsmallest(5).index[2], results[0].nsmallest(5).index[3], results[0].nsmallest(5).index[4]

print('The best ECM for this dataset is ' + str(ecmList[min1]) + ' with a chi^2 value of: ' + str(results.iloc[min1,0]) + ' and using model: ' + str(functions.iloc[min1,0]))
print('The second best ECM for this dataset is ' + str(ecmList[min2]) + ' with a chi^2 value of: ' + str(results.iloc[min2,0])+ ' and using model: ' + str(functions.iloc[min2,0]))
print('The third best ECM for this dataset is ' + str(ecmList[min3]) + ' with a chi^2 value of: ' + str(results.iloc[min3,0])+ ' and using model: ' + str(functions.iloc[min3,0]))
print('The fourth best ECM for this dataset is ' + str(ecmList[min4]) + ' with a chi^2 value of: ' + str(results.iloc[min4,0])+ ' and using model: ' + str(functions.iloc[min4,0]))
print('The fifth best ECM for this dataset is ' + str(ecmList[min5]) + ' with a chi^2 value of: ' + str(results.iloc[min5,0])+ ' and using model: ' + str(functions.iloc[min5,0]))