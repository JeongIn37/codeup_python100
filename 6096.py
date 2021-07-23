grid = []

#19*19 grid 생성
for i in range(20):
    grid.append([])
    for j in range(20):
        grid[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        grid[i+1][j+1] = int(a[j])

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    for j in range(1,20):
        if grid[j][y]==0:
            grid[j][y]=1
        else:
            grid[j][y]=0
        if grid[x][j]==0:
            grid[x][j]=1
        else:
            grid[x][j]=0

for i in range(1,20):
    for j in range(1, 20):
        print(grid[i][j], end=" ")
    print()
