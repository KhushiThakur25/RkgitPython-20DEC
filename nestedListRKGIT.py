li = [[1,2,3],[4,5,6],[7,8,9]]
si = [[1,0,31],[1,3,1],[0,5,7]]
vi = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(li)):
    for j in range(len(li[0])):
        vi[i][j] = li[i][j]*si[i][j]

print(vi)
