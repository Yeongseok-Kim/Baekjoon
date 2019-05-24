# 별 찍기 - 5

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