h, w = input().split()
h = int(h)
w = int(w)

#w,h 크기를 바탕으로 판 그리기(0으로 초기화)
map = []
for i in range(h+1):
    map.append([])
    for j in range(w+1):
        map[i].append(0)

n = int(input())
for i in range(n):
    l, d, x, y = input().split()
    if int(d) == 0:
        for j in range(int(l)):
            map[int(x)][int(y)+j]=1
    else:   #d==1
        for j in range(int(l)):
            map[int(x)+j][int(y)]=1

#출력
for i in range(1, h+1):
    for j in range(1, w+1):
        print(map[i][j], end=" ")
    print()
