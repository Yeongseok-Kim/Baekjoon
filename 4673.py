# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다

def d(n):
    sum=n
    while n!=0:
        sum+=n%10
        n=n//10
    return sum

selfNumber=list(range(1,10001))

for i in range(1,10001):
    n=d(i)
    if n in selfNumber:
        selfNumber.remove(n)

for i in selfNumber:
    print(i)