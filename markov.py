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
leng = len(z)
pp, cc , pc, cp = 0, 0, 0, 0

# for PP
for x in range(0, leng  - 1):

    if(z[x] == 'p' and z[x+1] == 'p'):
        pp+=1
pp = pp / c
print("probability that a person drinks pepsi and will continue to do so: " +str(pp))

# for CC
for x in range(0, leng  - 1):

    if(z[x] == 'c' and z[x+1] == 'c'):
        cc+=1
cc = cc / c
print("probability that a person drinks cola and will continue to do so: " +str(cc))

# for PC
for x in range(0, leng  - 1):

    if(z[x] == 'p' and z[x+1] == 'c'):
        pc+=1
pc = pc / c
print("probability that a person drinks pepsi and will shift to cola is: " +str(pc))

# for CP
for x in range(0, leng  - 1):

    if(z[x] == 'c' and z[x+1] == 'p'):
        cp+=1
cp = cp / c
print("probability that a person drinks cola and will shift to pepsi is: " +str(cp))

ipm = [b, d]
ipm = np.matrix(ipm)
r1 = [pp, pc]
r2 = [cp, cc]
m = np.matrix((r1, r2))

for x in range(1, 3):
    ipm = np.dot(ipm, m)
    print("probability after " +str(x)+ " day is: " + str(ipm))
