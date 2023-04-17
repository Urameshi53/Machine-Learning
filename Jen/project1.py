# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:02:15 2022

@author: Ju5t1@e
"""

import pandas as pd
import matplotlib.pyplot as plt
file = r'C:\\Users\\User\\Documents\\Python\\Jen\\Data.xlsx' # Replacce with your file path

data = pd.read_excel(file)
gauge_2000 = data.loc[data['YEAR']==2000,'GAUGE DATA']
gauge_2001 = data.loc[data['YEAR']==2001,'GAUGE DATA']
satellite_2000 = data.loc[data['YEAR']==2000, 'SATELLITE DATA']
satellite_2001 = data.loc[data['YEAR']==2001, 'SATELLITE DATA']
month_2000 = data.loc[data['YEAR']==2000,'MONTH']
month_2001 = data.loc[data['YEAR']==2001,'MONTH']

plt.bar(gauge_2000,satellite_2000)
plt.xlabel('Gauge data')
plt.ylabel('Satellite data')
# plt.title('A graph of Gauge data against Satellite data (2000)')

plt.bar(gauge_2001,satellite_2001)
plt.xlabel('Gauge data')
plt.ylabel('Satellite data')
# plt.title('A graph of Gauge data against Satellite data (2001)')

# plt.bar(month_2000,gauge_2000)
# plt.xlabel('Month')
# plt.ylabel('Gauge data')

# plt.bar(month_2001,gauge_2001)
# plt.xlabel('Month')
# plt.ylabel('Gauge data')
# plt.title('A graph of')
plt.title('A graph of gauge data against satellite data in 2000 and 2001')
plt.show()

