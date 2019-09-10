def rev(n):
    result=0
    while n!=0:
        result*=10
        result+=n%10
        n=n//10
    return result

x,y=input().split()
x,y=int(x),int(y)
print(rev(rev(x)+rev(y)))