# 한수

def f(n):
    s=[]

    if n<100:
        return 1

    while n!=0:
        s.append(n%10)
        n=n//10
    
    for i in range(1,len(s)-1):
        if s[i-1]-s[i]!=s[i]-s[i+1]:
            return 0
    
    return 1

n=int(input())
result=0

for i in range(1,n+1):
    result+=f(i)

print(result)