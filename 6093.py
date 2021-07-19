n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

for i in range(n-1, -1, -1):    #(시작, 끝, 증감) => 시작 수는 포함, 끝은 미포함!!! 
    print(numbers[i], end=" ")