# 별 찍기 - 6

n=input()
n=int(n)

i=0
while i<n:
    k=0
    while k<i:
        print(" ",end='')
        k+=1
    j=0
    while j<=((n-i)*2-2):
        print("*",end='')
        j+=1
    print()
    i+=1