#입력조건: 첫째 줄에 N(2<N<1,000). M(1<M<10,000), K(1<K<10,000)
#자연수가 주어지며 각 자연수는 공백으로 구분한다
#둘째 줄에 N개의 자연수가 주어진다. 단 각각의 자연수는 1이상
#10,000 이하의 수로 주어진다; 입력으로 주어지는 K는 항상 M보다 작거나 같다

#문재해결을 위해서는 가장 큰 수 와 두번째로 큰수만 저장하면된다
#가장 큰 수를 K번 더하고 두번째로 큰 수를 한 번 더하는 연산을 반복한다

n,m,k= map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result=0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)