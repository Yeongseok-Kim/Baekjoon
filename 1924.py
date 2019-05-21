# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?

x,y=input().split()
day=0

for i in range(1,x+1):
    if i in [1,3,5,7,8,10,12]:
        day+=31
    elif i in [4,6,9,11]:
        day+=30
    else:
        day+=28

day+=y

if day%7==1:
    print("MON")
elif day%7==2:
    print("TUE")
elif day%7==3:
    print("WED")
elif day%7==4:
    print("THU")
elif day%7==5:
    print("FRI")
elif day%7==6:
    print("SAT")
else:
    print("SUN")