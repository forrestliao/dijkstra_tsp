import pandas as pd
import sys
from pprint import pprint

INF = sys.maxsize
e = np.zeros((10,10), dtype = np.int)

pprint(e)

n, m = map(int, input().split(' '))

# initialnize
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            e[i][j] = 0
        else:
            e[i][j] = INF 

#read lines
for line in range(1, m+1):
    t1, t2, t3 = map(int,input().split(" "))
    e[t1][t2] = t3

#Floyd algorithm
for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			if e[i][j] > e[i][k]+e[k][j]:
				e[i][j] = e[i][k]+e[k][j]


for i in range(1,n+1):
    print(e[i][1:n+1])

