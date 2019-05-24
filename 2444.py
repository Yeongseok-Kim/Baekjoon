# 별 찍기 - 7

n=input()
n=int(n)

i=0
while i<n:
    k=1
    while k<n-i:
        print(" ",end='')
        k+=1
    j=0
    while j<=(i*2):
        print("*",end='')
        j+=1
    print()
    i+=1

i=1
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