# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:04:10 2024

@author: quiks
"""

# --------------------------------------------------------- Necessary Libraries  ---------------------------------------------------------
import deareis          
import pandas as pd

# --------------------------------------------------------- Edit Data Path Here ----------------------------------------------------------
data = deareis.parse_data(r'C:\Users\quiks\OneDrive\Documents\SEEDS\DATA\EX21 16Hr PBS\240711 RMB EX21 Kai_#1.DTA')

# --------------------------------------------------------- Create Variables -------------------------------------------------------------
v, r = '(RC)', '(C[RW])'
ECM, results, functions = [], [], []

# --------------------------------------------------------- ECM Combination Generator ----------------------------------------------------
for i in range(1,10):  
    baby = 'R['
    baby = baby + v * i
    print(baby)
    ECM.append(baby + ']')
    ECM.append(baby + r + ']')  
    ECM.append(baby + ']W')       
    
for i in range(1,10):  
    baby = 'R(['
    baby = baby + v * i
    ECM.append(baby + '][' + r + '])') 
    ECM.append(baby + '][' + r + '])W') 
    ECM.append(baby + '][' + v + r + '])')
    ECM.append(baby + '][' + v + r + '])W')

for i in range(1,10):  
    baby = 'R(['
    baby = baby + v * i + r
    ECM.append(baby + '][' + r + '])') 
    ECM.append(baby + '][' + r + '])W') 
    ECM.append(baby + '][' + v + r + '])')
    ECM.append(baby + '][' + v + r + '])W')
           
ecmList = list(set(ECM)) 

# --------------------------------------------------------- ECM Fitter -------------------------------------------------------------------
for i in ecmList:
    #Valid method values: 'leastsq', 'least_squares', 'nelder', 'lbfgsb', 'powell', 'cg', 'bfgs', 'tnc', 'slsqp', and 'auto'
    settings = deareis.FitSettings(i, method = '15', weight = 'AUTO', max_nfev = 1000) 
    fit = deareis.fit_circuit(data[0], settings)
    results.append(fit.chisqr)
    functions.append(fit.method)
    print(len(results)/(len(ecmList)/100))

# --------------------------------------------------------- Best ECM Finder -------------------------------------------------------------    
results = pd.DataFrame(results)
functions = pd.DataFrame(functions)
min1, min2, min3, min4, min5 = results[0].nsmallest(5).index[:]

print('The best ECM for this dataset is ' + str(ecmList[min1]) + ' with a chi^2 value of: ' + str(results.iloc[min1,0]) + ' and using model: ' + str(functions.iloc[min1,0]))
print('The second best ECM for this dataset is ' + str(ecmList[min2]) + ' with a chi^2 value of: ' + str(results.iloc[min2,0])+ ' and using model: ' + str(functions.iloc[min2,0]))
print('The third best ECM for this dataset is ' + str(ecmList[min3]) + ' with a chi^2 value of: ' + str(results.iloc[min3,0])+ ' and using model: ' + str(functions.iloc[min3,0]))
print('The fourth best ECM for this dataset is ' + str(ecmList[min4]) + ' with a chi^2 value of: ' + str(results.iloc[min4,0])+ ' and using model: ' + str(functions.iloc[min4,0]))
print('The fifth best ECM for this dataset is ' + str(ecmList[min5]) + ' with a chi^2 value of: ' + str(results.iloc[min5,0])+ ' and using model: ' + str(functions.iloc[min5,0]))