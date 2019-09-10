def suger(n):
    if n%5==0:
        return n/5
    elif n%5==1:
        if n==1:
            return -1
        return (n-6)/5+2
    elif n%5==2:
        if n<12:
            return -1
        return (n-12)/5+4
    elif n%5==3:
        return (n-3)/5+1
    else:
        if n==4:
            return -1
        return (n-9)/5+3

n=int(input())
print(int(suger(n)))