#정수 2개(a, b)가 공백을 두고 입력된다. (0 <= a, b <= 10)
#a 를 2^b배 만큼 곱한 값을 출력한다.

a, b = map(int, input().split())
print(a<<b)