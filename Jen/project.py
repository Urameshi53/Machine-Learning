# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:12:40 2022

@author: User
"""

import matplotlib.pyplot as plt

def load(file):
    year = []
    month = []
    rain_temp = []
    with open(file,'r') as f:
        while True:
            t = f.readline()
            if not t:
                break
            t = t.split()
            year.append(t[0])
            month.append(t[1])
            rain_temp.append(t[2])
    f.close()

    return year,month,rain_temp 
        
file1 = r'C:\\Users\\User\\Documents\\Python\\Jen\\rain.txt'
file2 = r'C:\\Users\\User\\Documents\\Python\\Jen\\temp.txt'

def calculate_monthly(year,month,values):
    n = 0
    monthly = []
    monthly_values = {}
    year_modified = []
    while n <= 600:
        a = n
        n += 12
        if n > 600:
            break
        s = 0
        for i in range(a,n):
            s += float(values[i])
        monthly.append(round(s,2))
        year_modified.append(year[a])
    for i in range(len(year_modified)):
        monthly_values[year_modified[i]] = monthly[i]
    return monthly_values  

def calculate_yearly(monthly):
    yearly = monthly.copy()
    for i in monthly:
        yearly[i] = round(yearly[i]/12,2)
    return yearly
    

rain_year, rain_month, rain_values = load(file1)
temp_year, temp_month, temp_values = load(file2)
m_rain = calculate_monthly(rain_year, rain_month, rain_values)
m_temp = calculate_monthly(temp_year, temp_month, temp_values)
a_rain = calculate_yearly(m_rain)
a_temp = calculate_yearly(m_temp)


plt.scatter(m_rain.values(),m_temp.values())
plt.ylabel('temperature')
plt.xlabel('rain')
plt.show()


plt.scatter(a_rain.values(),a_temp.values())
plt.ylabel('temperature')
plt.xlabel('rain')
plt.show()
        

        