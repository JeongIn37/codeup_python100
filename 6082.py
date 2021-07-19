a = int(input())
for i in range(1,a+1):
    if i % 10 == 3:
        print("x", end=' ')
    elif i % 10 == 6:
        print("x", end=' ')
    elif i % 10 == 9:
        print("x", end=' ')
    else:
        print(i, end=' ')
    i += 1