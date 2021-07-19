a = int(input())

while True:
    for i in range(1, a+1):
        if i % 3 == 0:
            continue
        else:
            print(i, end=" ")
    if i == a:
        break
