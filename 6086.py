std = int(input())
i = 1
tmp = 0
while True:
    if tmp+i >= std:
        break
    tmp += i
    i += 1
print(tmp+i)
