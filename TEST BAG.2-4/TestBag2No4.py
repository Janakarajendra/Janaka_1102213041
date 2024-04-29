
X = [[12,7,8],
    [4 ,5,9],
    [3 ,8,7]]

result = [[0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):   
     for k in range(len(X[1])):
         result[j][i][k] = X[i][j][k]
        

for r in result:
   print(r)
