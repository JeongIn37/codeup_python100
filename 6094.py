n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])

numbers.sort()
print(numbers[0])

#sort 안 쓰고 작성하는 방법 익히기
# n = int(input())
# a = input().split()

# for i in range(n) :
#   a[i] = int(a[i])

# min = a[0]
# for i in range(0, n) :
#   if a[i] < min :
#     min = a[i]

# print(min)