# You can increase the N here to plot a larger scale free network
n = 8
PLIMIT = 0.5

from math import pow, floor
from pprint import pprint
from random import uniform
nodes = int(pow(3,n))

mat = [[1]]
index = 2
# print(mat)
for i in range(0,n):
    for x in range(len(mat)):
        newrow = []
        for t in range(len(mat[x])*2):
            newrow.append(index)
            index+=1
        mat.append(newrow)
    # print(mat)

matrix = [[0 for x in range(0, nodes) ] for y in range(0, nodes)]


def connect(x, y):
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

lastPow = 0
selRow = 1
while(selRow<len(mat)):
    for rootInd, rootValue in enumerate(mat[selRow]):
        connect(1, rootValue)
    lastPow += 1
    selRow  += 2**lastPow


for smallInd in range(2, len(mat), 2):
    for pInd, pValue in enumerate(mat[smallInd]):
        connect(pValue, mat[smallInd+1][(2*pInd) + 0])
        connect(pValue, mat[smallInd+1][(2*pInd) + 1])


rind = 0
while (rind < len(mat)):
    off = 0
    for re in mat[rind]:
      if (uniform(0.0, 1.0) <= PLIMIT):
        connect(re, mat[rind+3][(4*off) + 0])
        connect(re, mat[rind+3][(4*off) + 1])
        connect(re, mat[rind+3][(4*off) + 2])
        connect(re, mat[rind+3][(4*off) + 3])
    rind+=4


def mprint(mat =[]):
    for row in mat:
        print(row)

# mprint(matrix)


# Just to check if all the nodes are connected
# should ideally print nothing

for ind, row in enumerate(matrix):
  if(1 not in row):
    print(ind)

import csv

with open("t.csv","w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerow([x for x in range(0, len(matrix)+1)])
    for index, row in enumerate(matrix):
      csvWriter.writerow([index+1] + row)
