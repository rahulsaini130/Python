from numpy import *

m1 =   matrix('1 3 4 ; 5 6 7 ; 2 3 5' )
m2 =   matrix('8 9 11; 12 13 4; 21 2 3')

#print(m1.shape)
m1_rows, m1_cols = m1.shape
m2_rows, m2_cols = m2.shape
arr = []
a = 0
#print(range(m1_rows))
for x in range(m1_rows):
    for y in range(m2_cols):
        for z in range(m1_rows):
            a += (m1[x,z] * m2[z,y])
        arr.append(a)
        a = 0
i = asarray(arr)
e = i.reshape(3,3)
print(e)

