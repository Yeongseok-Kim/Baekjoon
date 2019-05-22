# 한수

def f(n):
    if n<100:
        return 1
    s0=n%10
    n=n//10
    s1=n%10
    n=n//10
    s2=n%10

    if (s0-s1)==(s1-s2):
        return 1
    else:
        return 0

n=int(input())
result=0

for i in range(1,n+1):
    result+=f(i)

print(result)