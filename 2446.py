# 별 찍기 - 9

n=input()
n=int(n)

i=0
while i<n:
    j=0
    while j<i:
        print(" ",end='')
        j+=1
    
    j=0
    while j<(n-i)*2-1:
        print("*",end='')
        j+=1
    print()
    i+=1

i=2
while i<=n:
    j=0
    while j<(n-i):
        print(" ",end='')
        j+=1

    j=0
    while j<i*2-1:
        print("*",end='')
        j+=1
    print()
    i+=1