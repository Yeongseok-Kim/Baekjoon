# 별 찍기 - 3

n=input()
n=int(n)

i=0
while i<n:
    j=0
    while j<n-i:
        print("*",end='')
        j+=1
    print()
    i+=1