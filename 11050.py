def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

n,k=input().split()
n,k=int(n),int(k)

if k<0 or k>n:
    print("0")
else:
    result=factorial(n)//(factorial(k)*factorial(n-k))
    print(result)