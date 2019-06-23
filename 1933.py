n=input()
n=int(n)
s=[]
while n>0:
    l,h,r=input().split()
    l,h,r=int(l),int(h),int(r)
    for i in range(l,r):
        while len(s)<=r:
            s.append(0)
        if s[i]<h:
            s[i]=h
    n-=1
for i in range(len(s)):
    if s[i]!=s[i-1]:
        print(i,s[i],end=' ')