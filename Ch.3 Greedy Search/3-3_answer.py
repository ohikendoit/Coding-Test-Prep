#숫자카드게임-1
#n,m을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)