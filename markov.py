import csv
import pandas
import numpy as np
from datascience import *
a = Table.read_table('brand.csv')
e = pandas.read_csv('brand.csv', header = 0)
z = e.brand.tolist()
print(z)
c = a.num_rows
b = a.select('brand').where('brand', 'p').num_rows
b = b / c
d = 1 - b
count = 0
for x in z:
    i1 = int(z.index(x))
    i2 = int(i1 + 1)
    print(i1,i2)
    if(z[i1] == 'p' and z[i2] == 'p'):
        print(z[i1], z[i2])
        count+=1
        print(count)