from itertools import groupby

numbers = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
big = 0
for i,j in groupby(numbers):
     d = list(j)
     if i==1:
          if len(d)>big:
               big=len(list(d))
print('maximum consecutive 1 are :',big)

