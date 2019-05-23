#평균이 넘는 학생들의 퍼센테이지를 출력하는 문제

i=input()
i=int(i)
result=[]

while i>0:
    s=input().split()
    s=list(map(float,s))
    j=1
    sumResult=0
    sumResult=float(sumResult)
    while s[0]>=j:
        sumResult+=s[j]
        j+=1
    average=sumResult/s[0]
    overAverage=0
    j=1
    while s[0]>=j:
        if average<s[j]:
            overAverage+=1
        j+=1
    result.append(round((overAverage/s[0])*100,3))
    i-=1

for i in result:
    print('%.3f'%i,end='')
    print("%")