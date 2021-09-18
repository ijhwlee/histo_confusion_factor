#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from histo_confusion import *

file_names = []
for idx in range(7):
    file_name = "LIKELIHOOD.injection.event0.v{0}.dat".format(idx+1)
    file_names.append(file_name)

cf_list_normalized = calc_confusion_factors(file_names, 100, 'log_Normalized[28]')
cf_list_undecomposed = calc_confusion_factors(file_names, 100, 'log_Undecomposed[26]')


print("Normalized = {0}".format(cf_list_normalized))
print("Undecomposed = {0}".format(cf_list_undecomposed))


plt.plot(cf_list_normalized)
plt.title("Log Normalized")
plt.show()


plt.plot(cf_list_undecomposed)
plt.title("Log Undecomposed")
plt.show()




