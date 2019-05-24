# X보다 작은 수

n,x=input().split()
n=int(n)
x=int(x)
s=input().split()
s=list(map(int,s))
i=0

while i<n:
    if s[i]<x:
        print(s[i],end=' ')
    i+=1