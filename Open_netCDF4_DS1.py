import netCDF4
import numpy as np
from netCDF4 import Dataset
 
volcgrp = Dataset('Data Science Collection_Chandan_Troughia_DS1.nc', 'r')
print(volcgrp)
print('Following are the variable names:')

for i in  volcgrp.variables:
    print(i)
print('='*80)
print()
#make a list to display data in each column
b = []

print('Data is below:\n')
list_a = ['Time','Age_in_years','Gender','Monthly_Rent','Food_Expenses','Internet_Expenses','Phone_Expenses','Laundry_Expenses','Other_Expenses']
for item in list_a:
    b = (volcgrp.variables[item][:])
    print(item)
    print()
    print(b)
    print('='*80)
    print()
#============================Print Metadata_DS1.nc==========================    
volcgrp1 = Dataset('Metadata_DS1.nc', 'r')
print(volcgrp1)
print('Following are the variable names:')
for i in volcgrp1.variables:
    print(i)
print('='*80)
print()

m = []
print('Data is below:\n')
list_m = ['Name','Meaning']
for item in list_m:
    m = (volcgrp1.variables[item][:])
    print(item)
    print()
    print(m)
    print('='*80)
    print()
#============================Print Provenance_DS1.nc=======================
volcgrp2 = Dataset('Porvenance_DS1.nc', 'r')
print(volcgrp2)
print('Following are the variable names:')
for i in volcgrp2.variables:
    print(i)
print('='*80)
print()

p = []
print('Data is below:\n')
list_p = ['Name','Meaning']
for item in list_p:
    p = (volcgrp2.variables[item][:])
    print(item)
    print()
    print(p)
    print('='*80)
    print()