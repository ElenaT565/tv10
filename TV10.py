import numpy as np
import scipy as stats
import matplotlib as plt
import pandas as pd
import scipy.stats as ss

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182, 179.125, 179.125, 179.125])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180, 178.666, 178.666])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

k = 3
n = 28

y_mean_1 = np.mean(y1)
print(y_mean_1)
#179.125
y_mean_2 = np.mean(y2)
print(y_mean_2)
#178.666
y_mean_3 = np.mean(y3)
print(y_mean_3)
#172.7272

total = np.array([y1, y2, y3])
print(total)
# total array
#[[173.    175.    180.    178.    177.    185.    183.    182.    179.125
# 179.125 179.125]
# [177.    179.    180.    188.    177.    172.    171.    184.    180.
# 178.666 178.666]
#[172.    173.    169.    177.    166.    180.    178.    177.    172.
# 166.    170.   ]]

y_mena_total = np.mean(total)
print(y_mena_total)
#176.83960606060606

print(np.sum((total - 176.85)**2)) #857.252587
S_f = np.sum((y_mean_1 - 176.85)**2)*11 + np.sum((y_mean_2 - 176.85)**2)*11 + np.sum((y_mean_3 - 176.85)**2)*11
print(S_f) #280.19576809090984
S_ost = np.sum((y1 - y_mean_1)**2) + np.sum((y2 - y_mean_2)**2) + np.sum((y3 - y_mean_3)**2)
print(S_ost) #577.0568189090909
#577.0568189090909 + 280.19576809090984 = 857.252587

D_f = S_f / ( k - 1)
print(D_f) #140.09788404545492
D_ost = S_ost / ( n - k )
print(D_ost) #23.082272756363636
F_n = D_f / D_ost
print(F_n) #6.069501280233803

f = ss.f_oneway(y1, y2, y3)
print(f)
#F_onewayResult(statistic=7.283308864612123, pvalue=0.0026404240873847064)

#табличное значение = 3,38
#F_n = 6,09