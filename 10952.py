result_list=[]

while True:
    a,b=input().split()
    a,b=int(a),int(b)

    if a==0 and b==0:
        break

    result_list.append(a+b)

for i in result_list:
    print(i)