# 별 찍기 - 8

n=input()
n=int(n)

i=1
while i<n:
    j=0
    while j<i:
        print("*",end='')
        j+=1
    
    j=0
    while j<(n-i)*2:
        print(" ",end='')
        j+=1
    
    j=0
    while j<i:
        print("*",end='')
        j+=1
    print()
    i+=1

i=0
while i<n*2:
    print("*",end='')
    i+=1
print()

i=1
while i<n:
    j=0
    while j<(n-i):
        print("*",end='')
        j+=1
    
    j=0
    while j<i*2:
        print(" ",end='')
        j+=1
        
    j=0
    while j<(n-i):
        print("*",end='')
        j+=1
    print()
    i+=1