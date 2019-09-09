a,b,c=input().split()
a,b,c=int(a),int(b),int(c)

if b>=a>=c or c>=a>=b:
    print(a)
elif a>=b>=c or c>=b>=a:
    print(b)
else:
    print(c)