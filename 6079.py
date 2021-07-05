a = int(input())
i = 1
sum = 0
while(True):
    sum += i
    i += 1
    if (a<=sum):
        print(i-1)
        break
